from kaizen.metrics import compute_security_metrics
from kaizen.drift import detect_distribution_drift
from kaizen.feedback import generate_feedback_dataset
from kaizen.retrain import retrain_model


def kaizen_loop(model, enriched_df, baseline_metrics):
    current_metrics = compute_security_metrics(enriched_df)
    drift_detected = detect_distribution_drift(current_metrics, baseline_metrics)

    if not drift_detected:
        print("No drift detected.")
        return model, baseline_metrics

    print("Drift detected. Initiating Kaizen retraining...")
    feedback_df = generate_feedback_dataset(enriched_df)
    updated_model = retrain_model(model, feedback_df)
    return updated_model, current_metrics