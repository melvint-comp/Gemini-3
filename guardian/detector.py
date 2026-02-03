def detect(features):
    """
    Applies simple rule-based detection logic.
    Returns a detection result dictionary.
    """

    if features["identity_mismatch"]:
        result = {
            "suspicious": True,
            "score": 0.9,
            "reason": "caller_identity_does_not_match_key_owner"
        }
    else:
        result = {
            "suspicious": False,
            "score": 0.1,
            "reason": "identity_matches_key_owner"
        }

    return result


if __name__ == "__main__":
    # Local test without wiring the whole system yet
    sample_features = {
        "identity_mismatch": True,
        "access_hour": 1,
        "region": "europe-west1",
        "authorized_flag": False
    }

    detection = detect(sample_features)

    print("Detection Result:")
    for key, value in detection.items():
        print(f"{key}: {value}")

