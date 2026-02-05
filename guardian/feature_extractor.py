def extract_features(log):
    return [
        log["hour"],
        log["region_risk"],
        log["identity_mismatch"],
        log["key_sensitivity"],
        log["request_frequency"]
    ]