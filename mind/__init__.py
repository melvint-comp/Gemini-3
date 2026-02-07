import joblib
from sklearn.preprocessing import StandardScaler
from synthesize_data import synthesize_cloud_csv
from build_sen_model import build_security_enrichment_model
from train_model import train_model
from enrich_events import enrich_events

if __name__ == "__main__":
    df = synthesize_cloud_csv(10000)
    X = df.iloc[:, :10].values

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    y = [
        df["identity_mismatch"].values,
        df["unusual_time"].values,
        df["region_risk"].values,
        df["request_frequency"].values,
        df["possibility_of_fraud"].values,
    ]

    model = build_security_enrichment_model(X_scaled.shape[1])
    train_model(model, X_scaled, y)

    enriched_events = enrich_events(df, model)
    print(enriched_events.head())
    enriched_events.to_csv("output_file.csv", index = False)

    # Model Export/Deployment
    model.save("kc_ids_model.keras")
    joblib.dump(scaler, "feature_scaler.joblib")