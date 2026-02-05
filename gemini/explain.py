import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

def explain(log, score):
    prompt = f"""
    Analyze this cloud access event and explain why it may be suspicious:

    Event: {log}
    Fraud score: {score}

    Respond in clear, human-readable security language.
    """

    model = genai.GenerativeModel("gemini-1.5-pro")
    return model.generate_content(prompt).text