from fastapi import FastAPI

from backend.app.database.connection import engine
from backend.app.database.base import Base
from backend.app.database import models
from backend.app.api.routes import router

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="MailBrain",
    version="0.1.0",
    description="An AI-powered Email Productivity Platform"
)

# Register all API routes
app.include_router(router)


@app.get("/")
def root():
    return {
        "project": "MailBrain",
        "status": "Running",
        "version": "0.1.0"
    }