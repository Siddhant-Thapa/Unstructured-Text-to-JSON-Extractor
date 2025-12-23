from fastapi import APIRouter
from app.schemas import ExtractRequest, ExtractResponse

router = APIRouter()

@router.post("/extract", response_model= ExtractResponse)
def extract_data(request: ExtractRequest):
    dummy_data = {
        "example_field": "This is a placeholder",
        "another_field": None
    }

    return ExtractResponse(
        status="success",
        schema_type=request.schema_type,
        data=dummy_data
    )
