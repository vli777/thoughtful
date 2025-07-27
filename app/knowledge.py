import os
import json
import re

KB_PATH = os.getenv("KB_PATH", "data/kb.json")

def normalize(text: str) -> str:
    # strip out punctuation, lowercase, collapse spaces
    cleaned = re.sub(r"[^\w\s]", "", text)
    return cleaned.strip().lower()

def load_knowledge_base() -> dict[str, str]:
    """
    Load the KB and normalize all keys (strip punctuation + lowercase).
    """
    with open(KB_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    # detect formats…
    if isinstance(data, dict) and "questions" in data:
        items = data["questions"]
    elif isinstance(data, dict):
        # direct Q→A mapping
        items = [{"question": q, "answer": a} for q,a in data.items()]
    elif isinstance(data, list):
        items = data
    else:
        raise ValueError(f"Invalid KB format: {type(data)}")

    kb_map: dict[str, str] = {}
    for item in items:
        q = item.get("question")
        a = item.get("answer")
        if isinstance(q, str) and isinstance(a, str):
            kb_map[normalize(q)] = a

    return kb_map
