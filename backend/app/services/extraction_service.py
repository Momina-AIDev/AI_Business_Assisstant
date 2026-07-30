import os
import json

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

EMPTY_LEAD = {
    "name": None,
    "phone": None,
    "intent": None,
    "date": None,
    "time": None,
    "party_size": None,
}

EXTRACTION_PROMPT = """
You are an information extraction assistant.

Extract information ONLY from what the customer explicitly says.

Return EXACTLY one valid JSON object.

{
    "name": null,
    "phone": null,
    "intent": null,
    "date": null,
    "time": null,
    "party_size": null
}

Rules:

- Return ONLY JSON.
- No markdown.
- No explanations.
- Use null if information is missing.
- Never invent information.
- Never guess.
- Never normalize dates.
- Never normalize times.
- Preserve the customer's wording exactly.
- Preserve names exactly as written.
- Preserve phone numbers exactly as written.
- If multiple values are given, keep the latest one.
"""


def extract_lead(messages: list) -> dict:

    conversation = [
        {
            "role": "system",
            "content": EXTRACTION_PROMPT,
        }
    ]

    conversation.extend(messages)

    try:

        response = client.chat.completions.create(
            model="openai/gpt-oss-20b:free",
            messages=conversation,
        )

        content = (response.choices[0].message.content or "").strip()

        if not content:
            return EMPTY_LEAD.copy()

        return json.loads(content)

    except Exception as e:
        print(f"[Extraction Error] {e}")
        return EMPTY_LEAD.copy()