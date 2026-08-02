from fastapi import FastAPI

app = FastAPI(
    title="MailBrain",
    version="0.1.0",
    description="An AI-powered Email Productivity Platform"
)


@app.get("/")
def root():
    return {
        "project": "MailBrain",
        "status": "Running",
        "version": "0.1.0"
    }