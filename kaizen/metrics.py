def compute_security_metrics(enriched_df):
    return {
        "avg_fraud_score": enriched_df["possibility_of_fraud"].mean(),
        "high_risk_rate": (enriched_df["possibility_of_fraud"] > 0.7).mean(),
        "identity_mismatch_rate": enriched_df["identity_mismatch"].mean(),
        "request_freq_risk": enriched_df["request_frequency"].mean(),
    }