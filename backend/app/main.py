from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Unstructured text to JSON extractor")

app.include_router(router)

@app.get("/")
def health_check():
    return {"status": "Backend is running"}
