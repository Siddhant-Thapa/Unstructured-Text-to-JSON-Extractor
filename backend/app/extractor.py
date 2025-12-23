import os
import requests
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"   #calling llm via openrouter


def extract_with_llm(schema: dict, input_text: str) -> str:
    if not OPENROUTER_API_KEY:
        raise RuntimeError("OPENROUTER_API_KEY is not set")

    json_template = {key: None for key in schema.keys()}

    prompt = f"""
You are a strict information extraction engine.

Your task is to extract data from the text and populate the JSON object below.

Rules:
- Use ONLY the keys present in the JSON
- If a value is not explicitly present in the text, keep it null
- Do NOT guess or infer
- Do NOT add or remove keys
- Return ONLY valid JSON, nothing else

JSON format:
{json_template}

Text:
\"\"\"
{input_text}
\"\"\"
"""

    payload = {
       "model": "anthropic/claude-3-haiku",
        "messages": [
            {
                "role": "system",
                "content": "You extract structured data and output JSON only."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.0
    }

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        OPENROUTER_URL,
        headers=headers,
        json=payload,
        timeout=30
    )

    response.raise_for_status()

    # return response.json()["choices"][0]["message"]["content"]
    raw_content = response.json()["choices"][0]["message"]["content"]
    print("LLM RAW OUTPUT:\n", raw_content)

    return raw_content
