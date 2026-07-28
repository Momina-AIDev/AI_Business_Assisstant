import json
from pathlib import Path

LEADS_FILE = Path("app/storage/leads.json")


def save_lead(name: str, phone: str, inquiry: str):
    with open(LEADS_FILE, "r") as file:
        leads = json.load(file)

    leads.append(
        {
            "name": name,
            "phone": phone,
            "inquiry": inquiry,
        }
    )

    with open(LEADS_FILE, "w") as file:
        json.dump(leads, file, indent=4)

if __name__ == "__main__":
    save_lead(
        "Tom",
        "03001234567",
        "Interested in booking a table",
    )