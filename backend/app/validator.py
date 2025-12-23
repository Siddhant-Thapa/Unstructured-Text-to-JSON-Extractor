import json
import re

CURRENCY_MAP = {
    "₹": "INR",
    "$": "USD",
    "€": "EUR",
    "£": "GBP"
}

def _normalize_json_text(text: str) -> str:
    
    # Remove markdown code fences
    text = text.replace("```json", "").replace("```", "").strip()

    # Replace smart quotes with normal quotes
    text = text.replace("“", "\"").replace("”", "\"")
    text = text.replace("‘", "'").replace("’", "'")

    # Extract first JSON block
    match = re.search(r"\{[\s\S]*\}", text)
    if not match:
        raise ValueError("No JSON object found in LLM output")

    json_text = match.group(0)

    # Convert single quotes to double quotes (JSON requires double quotes)
    json_text = re.sub(r"'", "\"", json_text)

    return json_text


def validate_and_merge(schema: dict, llm_output: str) -> dict:
  

    json_text = _normalize_json_text(llm_output)

    try:
        parsed = json.loads(json_text)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON structure after normalization: {e}")

    result = schema.copy()

    for key in result:
        if key in parsed:
            result[key] = parsed[key]

    # Normalize currency if applicable
    if "currency" in result and result["currency"] in CURRENCY_MAP:
        result["currency"] = CURRENCY_MAP[result["currency"]]

    return result
