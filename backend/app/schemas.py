from pydantic import BaseModel
from typing import Any, Dict

class ExtractRequest(BaseModel):
    schema_type:str
    input_text:str

class ExtractResponse(BaseModel):
    status:str
    schema_type:str
    data: Dict[str,Any]
