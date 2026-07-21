
from fastapi import FastAPI
from app.api.chat import router as chat_router
from fastapi.middleware.cors import CORSMiddleware 

app = FastAPI(
    title="AI Business Assistant",
    description="AI Agent for customer support and lead qualification",
    version="1.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router)


@app.get("/")
def home():
    return {
        "message": "AI Business Agent API running"
    }