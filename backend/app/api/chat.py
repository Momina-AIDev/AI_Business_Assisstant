from fastapi import APIRouter
from pydantic import BaseModel
from app.services.ai_service import generate_reply

router = APIRouter()


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    reply: str


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    reply = generate_reply(request.message)

    return ChatResponse(
        reply=reply
    )