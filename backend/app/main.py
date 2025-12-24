from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router

app = FastAPI(title="Unstructured Text to JSON Extractor")

# enabling CORS
app.add_middleware(
    CORSMiddleware,
     allow_origins=[
        "http://localhost:5173",               # local development
        "https://text-to-json-frontend-final.vercel.app/"  # production frontend  https://text-to-json-frontend-final.vercel.app/
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/")
def health_check():
    return {"status": "Backend is running"}
