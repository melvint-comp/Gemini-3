def generate_feedback_dataset(enriched_df):

    confident_events = enriched_df[
        (enriched_df["possibility_of_fraud"] > 0.85) |
        (enriched_df["possibility_of_fraud"] < 0.15)
    ]

    return confident_events.sample(
        frac = min(1.0, len(confident_events) / len(enriched_df)),
        random_state = 42
    )