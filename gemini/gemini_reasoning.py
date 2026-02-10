import os
import json
import requests
from typing import Dict, Any

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY is not set")

# This is the only guaranteed working endpoint for your key
MODEL = "models/gemini-3-flash-preview"
BASE_URL = "https://generativelanguage.googleapis.com/v1beta"

def call_gemini(prompt: str) -> str:
    """
    Make a direct REST call to Gemini 2.5 Flash
    and return the raw text output.
    """
    url = f"{BASE_URL}/{MODEL}:generateContent?key={API_KEY}"
    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    response = requests.post(
        url,
        headers={"Content-Type": "application/json"},
        data=json.dumps(payload),
        timeout=30
    )

    if response.status_code != 200:
        raise RuntimeError(
            f"Gemini API failed ({response.status_code}): {response.text}"
        )

    data = response.json()
    return data["candidates"][0]["content"]["parts"][0]["text"]


def explain_with_gemini(enriched_event: Dict[str, Any]) -> Dict[str, Any]:
    """
    Build a structured reasoning prompt, send it to Gemini,
    and parse the JSON response.
    """
    prompt = (
        "You are a senior cloud security analyst.\n"
        "You are given one enriched cloud access event. "
        "Analyze the security risk and recommend actions.\n"
        "Respond ONLY with valid JSON using this schema:\n"
        "{\n"
        "  \"summary\": string,\n"
        "  \"attack_pattern\": string,\n"
        "  \"confidence_level\": one of [low, medium, high],\n"
        "  \"key_signals\": array of strings,\n"
        "  \"recommended_actions\": array of strings\n"
        "}\n"
        "Here is the event:\n"
        f"{json.dumps(enriched_event, indent=2)}"
    )

    raw = call_gemini(prompt)

    try:
        return json.loads(raw)
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Failed to parse JSON from Gemini: {e}\nRaw: {raw}")
