from guardian.feature_extractor import extract_features
from guardian.detector import detect
from gemini.explain import explain

fake_log = {
    "hour": 2,
    "region_risk": 0.85,
    "identity_mismatch": 1,
    "key_sensitivity": 0.9,
    "request_frequency": 15
}

features = extract_features(fake_log)
score = detect(features)
reason = explain(fake_log, score)

print("Fraud Score:", score)
print("Explanation:", reason)