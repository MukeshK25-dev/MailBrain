from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.database.base import Base
from backend.app.database.connection import engine
from backend.app.database import models

from backend.app.api.routes import router
from backend.app.api.auth_routes import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="MailBrain",
    description="An AI-powered Email Productivity Platform",
    version="0.1.0",
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "MailBrain API is running"
    }