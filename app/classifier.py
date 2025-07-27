import os
import json
from llm_client import client, DEFAULT_MODEL
from knowledge import load_knowledge_base

CLASSIFIER_MODEL = os.getenv("OPENAI_CLASSIFIER_MODEL", DEFAULT_MODEL)

def classify_question(user_input: str) -> str:
    """
    Return best matching KB question or 'None'.
    """
    kb = load_knowledge_base()
    questions = list(kb.keys())
    system_prompt = (
        "You are a semantic classifier. Choose the one question from the list that best matches user input, or 'None'."
    )
    user_prompt = (
        "Known questions:\n" + json.dumps(questions, indent=2)
        + f"\n\nUser query: \"{user_input}\"\nRespond with exactly one known question or 'None'."
    )
    resp = client.chat.completions.create(
        model=CLASSIFIER_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    msg = resp.choices[0].message.content
    return msg.strip() if isinstance(msg, str) and msg.strip() else "None"