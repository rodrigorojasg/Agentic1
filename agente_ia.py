import os
import sys
import google.generativeai as genai


def generar_hola_mundo(lenguaje: str) -> str:
    prompt = f"""
Genera un ejemplo mínimo y correcto de "Hola Mundo"
en el lenguaje {lenguaje}.

Reglas:
- Devuelve SOLO código
- Sin explicaciones
- Sin markdown
"""

    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

    model = genai.GenerativeModel(
        model_name="models/gemini-1.5-flash"
    )

    response = model.generate_content(
        prompt,
        generation_config={
            "temperature": 0.2,
            "max_output_tokens": 300
        }
    )

    return response.text.strip()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python agente_ia.py <lenguaje>")
        sys.exit(1)

    if not os.getenv("GOOGLE_API_KEY"):
        print("ERROR: Falta GOOGLE_API_KEY")
        sys.exit(1)

    lenguaje = sys.argv[1]
    print(generar_hola_mundo(lenguaje))
