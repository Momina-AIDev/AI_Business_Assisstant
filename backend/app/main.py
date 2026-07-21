
from fastapi import FastAPI
from app.api.chat import router as chat_router

app = FastAPI(
    title="AI Business Assistant",
    description="AI Agent for customer support and lead qualification",
    version="1.0"
)


app.include_router(chat_router)


@app.get("/")
def home():
    return {
        "message": "AI Business Agent API running"
    }