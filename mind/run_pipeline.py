from synthesize_data import synthesize_cloud_csv
from build_sen_model import build_security_enrichment_model
from train_model import train_model
from enrich_events import enrich_events

def run_pipeline():
    df = synthesize_cloud_csv(10000)
    X = df.iloc[:, :10].values

    y = [
        df["identity_mismatch"].values,
        df["unusual_time"].values,
        df["region_risk"].values,
        df["request_frequency"].values,
        df["possibility_of_fraud"].values,
    ]

    model = build_security_enrichment_model(X.shape[1])
    train_model(model, X, y)
    return enrich_events(df, model)