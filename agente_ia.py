import os
import sys
from google import genai


def run_agent():
    language = sys.argv[1] if len(sys.argv) > 1 else "Python"
    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        print("ERROR: GOOGLE_API_KEY no está configurada.")
        return

    prompt = (
        f"Generate ONLY the source code for a minimal "
        f"'Hello World' program in {language}. "
        f"No explanations. No markdown."
    )

    try:
        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
        )

        if not response or not response.text:
            print("ERROR: Respuesta vacía del modelo.")
            return

        print(response.text.strip())

    except Exception as e:
        # 👇 IMPORTANTE: no romper el job
        print(f"ERROR generando código: {e}")


if __name__ == "__main__":
    run_agent()
