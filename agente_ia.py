import os
import sys
import json
from openai import OpenAI

OUTPUT_FILE = "generated_files.txt"

def run_agent():
    if len(sys.argv) < 3:
        print("::error::Uso: python agente_ia.py '<stack>' '<historia>'")
        sys.exit(1)

    stack = sys.argv[1]
    historia = sys.argv[2]

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("::error::OPENAI_API_KEY no configurada")
        sys.exit(1)

    client = OpenAI(api_key=api_key)

    prompt = f"""
Eres un generador de proyectos de software.

Stack: {stack}
Historia de usuario: {historia}

Devuelve SOLO un JSON con esta estructura exacta:

{{
  "files": [
    {{
      "path": "ruta/del/archivo",
      "content": "contenido completo del archivo"
    }}
  ]
}}

Reglas:
- Código mínimo pero funcional
- Usa exclusivamente el stack tecnológico entregado, si el stack no es conocido usa el màs comùn par ese tipo de requerimientos.
- Sin markdown
- Sin explicaciones
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    try:
        data = json.loads(response.choices[0].message.content)
    except Exception:
        print("::error::Respuesta del modelo no es JSON válido")
        print(response.choices[0].message.content)
        sys.exit(1)

    created_files = []

    for f in data["files"]:
        path = f["path"]

        dir_name = os.path.dirname(path)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)

        with open(path, "w", encoding="utf-8") as file:
            file.write(f["content"])

        created_files.append(path)
        print(f"Creado: {path}")


    # Guardamos listado para el Action
    with open(OUTPUT_FILE, "w") as f:
        for path in created_files:
            f.write(path + "\n")

if __name__ == "__main__":
    run_agent()
