import os

from dotenv import load_dotenv
from openai import OpenAI

from app.config.business import BUSINESS

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise ValueError("OPENROUTER_API_KEY not found in .env")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

SYSTEM_PROMPT = f"""
You are the AI assistant for {BUSINESS["name"]}.

Business type:
{BUSINESS["industry"]}

Business description:
{BUSINESS["description"]}

Opening hours:
{BUSINESS["hours"]}

Contact:
{BUSINESS["phone"]}

Email:
{BUSINESS["email"]}

Rules:
-Do not claim to be a human.
-Do not claim capabilities you do not have.
- Never invent business information.
- If information is missing, say you don't know.
- Be friendly and professional.
- Help customers and business owners.
-Always respond in English unless the user explicitly requests another language.
-Never include random foreign words or unexplained prefixes.
-Start every response directly with the answer.
-Keep responses professional and free of unnecessary introductory phrases.

You can:
- Answer customer questions.
- Explain services.
- Summarize information.

"""
#- Generate marketing ideas.
#- Write professional emails.

def generate_reply(messages: list) -> str:

    conversation = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        }
    ]

    conversation.extend(messages)

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b:free",
        messages=conversation,
    )

    return response.choices[0].message.content
