from fastapi import APIRouter
from pydantic import BaseModel

from app.services.ai_service import generate_reply
from app.services.extraction_service import extract_lead
from app.services.lead_service import save_lead

router = APIRouter()


class ChatRequest(BaseModel):
    messages: list


class ChatResponse(BaseModel):
    reply: str


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    reply = generate_reply(request.messages)

    lead = extract_lead(request.messages)

    lead_saved = False

    if (
        lead.get("name")
        and lead.get("phone")
        and lead.get("intent")
    ):
        lead_saved = save_lead(
            name=lead["name"],
            phone=lead["phone"],
            inquiry=lead["intent"],
        )

    if lead_saved:
        reply += """

Thank you! Your request has been successfully recorded in our system.

A member of our team will contact you shortly to confirm the details.
"""

    return ChatResponse(reply=reply)