import json

CURRENCY_MAP = {
    "₹": "INR",
    "$": "USD",
    "€": "EUR",
    "£": "GBP"
}


def validate_and_merge(schema: dict, llm_output: str) -> dict:
   
    try:
        parsed = json.loads(llm_output)
    except json.JSONDecodeError:
        raise ValueError("LLM returned invalid JSON")

    result = schema.copy()

    for key in result.keys():
        if key in parsed:
            result[key] = parsed[key]

    # Normalize currency symbol to ISO code if present
    if "currency" in result and result["currency"] in CURRENCY_MAP:
        result["currency"] = CURRENCY_MAP[result["currency"]]

    return result
