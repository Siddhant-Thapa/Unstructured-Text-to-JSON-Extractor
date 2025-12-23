# This file contains all predefined extraction schemas.
# Schemas act as strict contracts for what the LLM is allowed to return.

SCHEMAS = {
    "contact_info": {
        "full_name": None,
        "email": None,
        "phone_number": None,
        "organization": None,
        "location": None,
    },
    "job_requirements": {
        "job_title": None,
        "required_skills": None,
        "experience_required": None,
        "location": None,
        "employment_type": None,
    },
    "invoice_info": {
        "invoice_number": None,
        "invoice_date": None,
        "total_amount": None,
        "currency": None,
        "due_date": None,
        "vendor_name": None,
    }
}
