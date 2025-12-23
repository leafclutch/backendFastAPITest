from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Leafclutch Backend Test")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for local testing only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "status": "Backend running successfully",
        "company": "Leafclutch Technologies"
    }

@app.get("/health")
def health_check():
    return {"health": "OK"}

@app.get("/api/test")
def api_test():
    return {
        "message": "API connection successful",
        "success": True
    }
