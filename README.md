# llm-hub

Tiny CLI to send one prompt to OpenAI, Anthropic or Gemini.

## Setup

```bash
pip install -r requirements.txt
```

Put your keys in `.env`:

```
OPENAI_API_KEY=...
ANTHROPIC_API_KEY=...
GEMINI_API_KEY=...
```

## Usage

```bash
python main.py openai "Explain DNS in one sentence"
python main.py anthropic "Write a haiku about git"
python main.py gemini "What is a monad?"
```
