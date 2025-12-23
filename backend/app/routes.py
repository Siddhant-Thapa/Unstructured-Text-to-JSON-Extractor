from fastapi import APIRouter, HTTPException
from app.schemas import ExtractRequest, ExtractResponse
from app.schema_store import SCHEMAS

router = APIRouter()

@router.post("/extract", response_model= ExtractResponse)
def extract_data(request: ExtractRequest):

    if request.schema_type not in SCHEMAS:
        raise HTTPException(
            status_code=400,
            detail="Unsupported schema type"
        )
    schema_template = SCHEMAS[request.schema_type].copy()
    
    return ExtractResponse(
        status="success",
        schema_type=request.schema_type,
        data=schema_template
    )
