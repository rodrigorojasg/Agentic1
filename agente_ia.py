import os
import sys
from openai import OpenAI


def run_agent():
    language = sys.argv[1] if len(sys.argv) > 1 else "Python"
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("ERROR: OPENAI_API_KEY no está configurada.")
        return

    prompt = (
        f"Generate ONLY the source code for a minimal "
        f"'Hello World' program in {language}. "
        f"No explanations. No markdown."
    )

    try:
        client = OpenAI(api_key=api_key)

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You generate source code only."},
                {"role": "user", "content": prompt},
            ],
            temperature=0,
            max_tokens=200,
        )

        code = response.choices[0].message.content.strip()
        print(code)

    except Exception as e:
        # ⚠️ NO romper el workflow
        print(f"ERROR generando código: {e}")


if __name__ == "__main__":
    run_agent()
