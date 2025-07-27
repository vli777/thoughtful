import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY", "").strip()
if not API_KEY:
    raise ValueError("Missing OPENAI_API_KEY in environment or .env file")

def _init_client():
    return OpenAI(api_key=API_KEY)

client = _init_client()
DEFAULT_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

def generic_fallback(question: str, store: bool = True) -> str:
    """
    Generate fallback answer via /v1/responses endpoint, parsing the 'output' for text.
    """
    response = client.responses.create(
        model=DEFAULT_MODEL,
        input=question,
        store=store
    )
    raw = response.json()
    # Ensure dict
    data = json.loads(raw) if isinstance(raw, str) else raw
    outputs = data.get("output")
    if not isinstance(outputs, list) or not outputs:
        return ""
    first = outputs[0]
    content_list = first.get("content") if isinstance(first, dict) else None
    if not isinstance(content_list, list):
        return ""
    for entry in content_list:
        if isinstance(entry, dict) and entry.get("type") == "output_text":
            text = entry.get("text")
            if isinstance(text, str):
                return text.strip()
    return ""
