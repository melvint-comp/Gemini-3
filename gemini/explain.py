import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

def explain(log, score):
    
    prompt = f"""
    You are reviewing the performance of a cloud intrusion
    detection system.

    Event:
    {log}

    Detection Verdict:
    {score}

    Tasks:
    1. Assess whether the system's reasoning appears sound.
    2. Identify any potential blind spots.
    3. Suggest one concrete improvement:
    - a feature
    - a threshold
    - or a behavioral signal

    Do NOT rewrite the system.
    Do NOT invent new data sources.
    Focus on incremental improvement.
    """

    model = genai.GenerativeModel("gemini-1.5-pro")
    return model.generate_content(prompt).text
    