import os
import sys
import google.generativeai as genai

def generar_hola_mundo(lenguaje: str) -> str:
    prompt = f"""
Genera un ejemplo mínimo y correcto de "Hola Mundo"
en el lenguaje {lenguaje}.

Requisitos:
- Solo código
- Sin explicaciones
- Usar convenciones estándar del lenguaje
"""

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)

    return response.text.strip()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python agente_ia.py <lenguaje>")
        sys.exit(1)

    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("ERROR: Falta la variable de entorno GOOGLE_API_KEY")
        sys.exit(1)

    genai.configure(api_key=api_key)

    lenguaje = sys.argv[1]
    codigo = generar_hola_mundo(lenguaje)

    print(codigo)
