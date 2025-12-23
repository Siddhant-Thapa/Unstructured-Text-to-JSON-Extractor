import os
import requests
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"   #calling llm via openrouter


def extract_with_llm(schema: dict, input_text: str,retries: int = 1) -> str:
    if not OPENROUTER_API_KEY:
        raise RuntimeError("OPENROUTER_API_KEY is not set")
    
    input_text = input_text.strip()
    if input_text.startswith('"') and input_text.endswith('"'):
        input_text = input_text[1:-1]
        

    json_template = {key: None for key in schema.keys()}

    prompt = f"""
You are a strict information extraction engine.

Your task is to extract data from the text and populate the JSON object below.

Rules:
- Output MUST be valid JSON
- Keys MUST be in double quotes
- Use ONLY the keys present in the JSON template
- If a value is not explicitly present, use null
- Do NOT include explanations, comments, or markdown
- Do NOT include trailing commas
- Return ONLY the JSON object


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
        "temperature": 0.0,
        "top_p": 1.0
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

    output = response.json()["choices"][0]["message"]["content"]

    # If first attempt fails, retry once with a stronger reminder
    if retries > 0:
        try:
            from app.validator import _normalize_json_text
            _normalize_json_text(output)
        except Exception:
            return extract_with_llm(schema, input_text, retries=retries - 1)

    return output

    # raw_content = response.json()["choices"][0]["message"]["content"]
    # # print("LLM RAW OUTPUT:\n", raw_content)

    # return raw_content
