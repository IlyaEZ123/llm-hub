import os
import sys

from dotenv import load_dotenv

load_dotenv()


def ask_openai(prompt: str) -> str:
    from openai import OpenAI

    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    r = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )
    return r.choices[0].message.content


def ask_anthropic(prompt: str) -> str:
    import anthropic

    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    r = client.messages.create(
        model="claude-sonnet-5-5",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )
    return r.content[0].text


def ask_gemini(prompt: str) -> str:
    from google import genai

    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    r = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
    return r.text


PROVIDERS = {
    "openai": ask_openai,
    "anthropic": ask_anthropic,
    "gemini": ask_gemini,
}


def main() -> None:
    if len(sys.argv) < 3 or sys.argv[1] not in PROVIDERS:
        print(f"Usage: python main.py <{'|'.join(PROVIDERS)}> \"your prompt\"")
        sys.exit(1)

    provider, prompt = sys.argv[1], " ".join(sys.argv[2:])
    print(PROVIDERS[provider](prompt))


if __name__ == "__main__":
    main()
