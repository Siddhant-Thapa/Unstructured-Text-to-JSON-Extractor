from fastapi import FastAPI

app = FastAPI(title="Unstructured text to JSON extractor")

@app.get("/")
def health_check():
    return {"status": "Backend is running"}
