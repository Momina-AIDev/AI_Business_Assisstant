import json
from pathlib import Path

STORAGE_PATH = Path(__file__).parent.parent / "storage"
LEADS_FILE = STORAGE_PATH / "leads.json"


def save_lead(name: str, phone: str, inquiry: str) -> bool:

    STORAGE_PATH.mkdir(exist_ok=True)

    if not LEADS_FILE.exists():
        LEADS_FILE.write_text("[]", encoding="utf-8")

    try:
        with open(LEADS_FILE, "r", encoding="utf-8") as f:
            leads = json.load(f)

            if not isinstance(leads, list):
                leads = []

    except (json.JSONDecodeError, FileNotFoundError):
        leads = []

    phone = phone.strip()

    for lead in leads:
        if lead.get("phone", "").strip() == phone:
            return False

    new_lead = {
        "name": name.strip(),
        "phone": phone,
        "inquiry": inquiry.strip(),
    }

    leads.append(new_lead)

    with open(LEADS_FILE, "w", encoding="utf-8") as f:
        json.dump(
            leads,
            f,
            indent=4,
            ensure_ascii=False,
        )

    return True