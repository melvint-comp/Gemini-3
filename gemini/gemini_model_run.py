import os
import csv
import json
import requests
from typing import List, Dict

# -------------------------
# Environment Key Setup
# -------------------------
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY environment variable is not set")

# Use the model that is confirmed to work with your key
MODEL = "models/gemini-2.5-flash"
BASE_URL = "https://generativelanguage.googleapis.com/v1beta"


def call_gemini(prompt: str) -> str:
    """
    Sends prompt to Gemini REST and returns the raw text response.
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
        timeout=60,
    )

    if response.status_code != 200:
        raise RuntimeError(
            f"Gemini API failed with status {response.status_code}:\n{response.text}"
        )

    data = response.json()
    return data["candidates"][0]["content"]["parts"][0]["text"]


def build_prompt_from_csv(csv_path: str) -> str:
    """
    Read the CSV file and select the top suspicious rows based on
    possibility_of_fraud, then build a prompt to send to Gemini.
    """
    rows = []

    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)

        for row in reader:
            try:
                score = float(row.get("possibility_of_fraud", 0))
            except:
                continue
            # store (score, row) pairs
            rows.append((score, row))

    if not rows:
        return "No rows found in CSV."

    # Sort by descending fraud score
    rows.sort(key=lambda x: x[0], reverse=True)

    # Take the top 3 most suspicious rows
    top_n = rows[:3]

    lines = [
        "Top suspicious model outputs from the CSV:\n"
    ]

    for score, r in top_n:
        # build a short description for each row
        # only include numeric values to shorten prompt
        description = ", ".join([f"{k}={v}" for k, v in r.items()])
        lines.append(f"Fraud Score: {score} -> {description}")

    lines.append(
        "\nPlease analyze these top suspicious records. Identify patterns, explain why they "
        "are suspicious, and recommend actions.\n"
        "Respond ONLY with valid JSON in this schema:\n"
        "{\n"
        "  \"summary\": string,\n"
        "  \"patterns\": [string],\n"
        "  \"recommended_actions\": [string]\n"
        "}"
    )

    return "\n".join(lines)


if __name__ == "__main__":
    # Resolve this script’s directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Build the relative path to the CSV
    csv_file = os.path.join(script_dir, "..", "mind", "notebooks", "output_file.csv")
    csv_file = os.path.normpath(csv_file)

    print("Using CSV file at:", csv_file)

    # Build the prompt 
    prompt_text = build_prompt_from_csv(csv_file)

    print("\n=== PROMPT SENT TO GEMINI ===\n")
    print(prompt_text[:800], "\n...")

    # Call Gemini and print the response
    gemini_response = call_gemini(prompt_text)

    print("\n=== GEMINI RESPONSE ===\n")
    print(gemini_response)
