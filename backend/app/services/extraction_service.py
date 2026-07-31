import os
import json
import re

from dotenv import load_dotenv
from openai import OpenAI
from app.services.parser import (
    extract_phone,
    extract_party_size,
    extract_date,
    extract_time,
    extract_intent,
)
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

- Return ONLY valid JSON.
- No markdown.
- No explanations.
- No extra text.
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

        print("\n===== RAW EXTRACTION =====")
        print(repr(content))
        print("==========================\n")

        if not content:
            return EMPTY_LEAD.copy()

        # Remove markdown
        content = content.replace("```json", "").replace("```", "").strip()

        # Find every JSON object
        matches = re.findall(r"\{.*?\}", content, re.DOTALL)

        if not matches:
            print("[Extraction Error] No JSON object found.")
            return EMPTY_LEAD.copy()

        # Use the LAST JSON object
        content = matches[-1]

        # Repair common free-model mistakes
        content = content.replace('null"', 'null')
        content = content.replace('true"', 'true')
        content = content.replace('false"', 'false')

        lead = json.loads(content)

        # Latest user message
        latest_user_message = ""

        for message in reversed(messages):
            if message.get("role") == "user":
                latest_user_message = message.get("content", "")
                break

        # Python extraction (overrides AI if found)
        phone = extract_phone(latest_user_message)
        date = extract_date(latest_user_message)
        time = extract_time(latest_user_message)
        party_size = extract_party_size(latest_user_message)
        conversation_text = " ".join(
        message.get("content", "")
        for message in messages
        if message.get("role") == "user"
)

        intent = extract_intent(conversation_text)

        if phone:
            lead["phone"] = phone

        if date:
            lead["date"] = date

        if time:
            lead["time"] = time

        if party_size:
            lead["party_size"] = party_size
        if intent:
            lead["intent"] = intent

        # Ensure all keys exist
        for key in EMPTY_LEAD:
            lead.setdefault(key, None)

        print("\n===== FINAL LEAD =====")
        print(lead)
        print("======================\n")

        return lead

    except Exception as e:
        print(f"[Extraction Error] {e}")
        return EMPTY_LEAD.copy()