def retrain_model(model, feedback_df):
    X = feedback_df.iloc[:, :10].values

    dummy_targets = [
        feedback_df["identity_mismatch"].values.reshape(-1, 1),
        feedback_df["unusual_time"].values.reshape(-1, 1),
        feedback_df["region_risk"].values.reshape(-1, 1),
        feedback_df["request_frequency"].values.reshape(-1, 1),
        feedback_df["possibility_of_fraud"].values.reshape(-1, 1),
    ]

    model.fit(X, dummy_targets, epochs = 5, batch_size = 32, verbose = 1)
    return model