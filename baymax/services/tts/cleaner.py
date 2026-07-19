import re

def clean_for_speech(text: str) -> str:
    text = re.sub(r'[\U00010000-\U0010ffff]', '', text)
    return text.strip()
