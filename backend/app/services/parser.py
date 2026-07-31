import re


def extract_phone(text: str):
    match = re.search(r'(?:\+92|0)\d[\d\s-]{8,13}', text)
    if match:
        return match.group().strip()
    return None


def extract_party_size(text: str):
    match = re.search(r'(\d+)\s*(?:people|persons|guests|friends|doston)', text, re.IGNORECASE)
    if match:
        return int(match.group(1))
    return None


def extract_date(text: str):
    text = text.lower()

    keywords = [
        "today",
        "tomorrow",
        "kal",
        "parson",
        "parso",
        "aaj"
    ]

    for word in keywords:
        if word in text:
            return word

    return None


def extract_time(text: str):

    patterns = [
        r'\d{1,2}:\d{2}\s?(?:am|pm)?',
        r'\d{1,2}\s?(?:am|pm)',
        r'\d{1,2}\s?bjy',
        r'\d{1,2}\s?baje'
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)

        if match:
            return match.group()

    return None

def extract_intent(text: str):

    text = text.lower()

    reservation_keywords = [
        "reserve",
        "reservation",
        "book",
        "booking",
        "table",
    ]

    menu_keywords = [
        "menu",
        "food",
        "dish",
        "pizza",
        "burger",
    ]

    hours_keywords = [
        "hours",
        "timing",
        "open",
        "close",
    ]

    location_keywords = [
        "location",
        "address",
        "where",
    ]

    if any(word in text for word in reservation_keywords):
        return "reservation"

    if any(word in text for word in menu_keywords):
        return "menu"

    if any(word in text for word in hours_keywords):
        return "hours"

    if any(word in text for word in location_keywords):
        return "location"

    return None