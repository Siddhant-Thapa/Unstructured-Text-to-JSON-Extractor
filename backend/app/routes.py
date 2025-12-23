from fastapi import APIRouter, HTTPException
from app.schemas import ExtractRequest, ExtractResponse
from app.schema_store import SCHEMAS
from app.extractor import extract_with_llm
from app.validator import validate_and_merge

router = APIRouter()

@router.post("/extract", response_model= ExtractResponse)
def extract_data(request: ExtractRequest):

    if request.schema_type not in SCHEMAS:
        raise HTTPException(
            status_code=400,
            detail="Unsupported schema type"
        )
    schema_template = SCHEMAS[request.schema_type].copy()

    try:
        llm_raw_output = extract_with_llm(
            schema= schema_template,
            input_text= request.input_text
        )
        extracted_data = validate_and_merge(
            schema= schema_template,
            llm_output= llm_raw_output
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
    
    return ExtractResponse(
        status="success",
        schema_type=request.schema_type,
        data=extracted_data
    )
