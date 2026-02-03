from datetime import datetime


def extract_features(event):
    """
    Extracts security-relevant features from a cloud access event.
    Returns a dictionary of features.
    """

    timestamp = datetime.fromisoformat(event["timestamp"])
    hour_of_day = timestamp.hour

    features = {
        "identity_mismatch": event["caller_identity"] != event["key_owner"],
        "access_hour": hour_of_day,
        "region": event["region"],
        "authorized_flag": event["authorized"]
    }

    return features


if __name__ == "__main__":
    # Local test without importing main.py yet
    sample_event = {
        "caller_identity": "service-account-c",
        "key_owner": "service-account-a",
        "resource": "kms-key-123",
        "timestamp": "2026-02-02T01:41:12.913842+00:00",
        "region": "europe-west1",
        "authorized": False
    }

    features = extract_features(sample_event)

    print("Extracted Features:")
    for key, value in features.items():
        print(f"{key}: {value}")

