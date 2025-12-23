import json

def validate_and_merge(schema:dict, llm_output: str) -> dict:
    try:
        parsed = json.loads(llm_output)
    except json.JSONDecodeError:
        raise ValueError("LLM returned invalid json")
    
    result = schema.copy()

    for key in result.keys():
        if key in parsed:
            result[key] = parsed[key]
    
    return result