from guardian.feature_extractor import extract_features
from guardian.detector import detect
from gemini.reasoning import explain_event
from kaizen.loop import kaizen_cycle

def run(event: dict):
    features = extract_features(event)
    verdict = detect(features)

    if verdict["suspicious"]:
        print("🚨 INCIDENT DETECTED\n")
        explanation = explain_event(event, features, verdict)
        print(explanation)

    kaizen_cycle(event, features, verdict)

if __name__ == "__main__":
    sample_event = {
        "caller_identity": "service-account-c",
        "key_owner": "service-account-a",
        "resource": "kms-key-123",
        "timestamp": "2026-02-02T01:41:12.913842+00:00",
        "region": "europe-west1",
        "authorized": False
    }

    run(sample_event)