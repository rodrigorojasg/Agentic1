import os
import sys
from google import genai


def run_agent():
    language = (
        os.getenv("INPUT_LANGUAGE")
        or (sys.argv[1] if len(sys.argv) > 1 else "Python")
    )

    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("::error::La variable GOOGLE_API_KEY no está configurada.")
        sys.exit(1)

    prompt = (
        f"Generate ONLY the source code for a minimal "
        f"'Hello World' program in {language}. "
        f"No explanations. No markdown."
    )

    try:
        genai.configure(api_key=api_key)

        # ⚠️ ÚNICO modelo estable hoy en v1beta
        model = genai.GenerativeModel("models/text-bison-001")

        response = model.generate_content(prompt)

        if not response or not response.text:
            raise RuntimeError("Respuesta vacía del modelo")

        print(response.text.strip())

    except Exception as e:
        print(f"::error::Error en el agente: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    run_agent()
