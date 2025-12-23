from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

app = FastAPI(title="Leafclutch Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://leafclutch.dev",
        "https://www.leafclutch.dev"
    ],
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
def health():
    return {"health": "OK"}

handler = Mangum(app)
