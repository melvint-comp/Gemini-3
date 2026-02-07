import pandas as pd
import numpy as np

def enrich_events(df, model):

    X = df.iloc[:, :10].values
    preds = model.predict(X)

    enrichment = pd.DataFrame(np.hstack(preds), columns=[
        "identity_mismatch",
        "unusual_time",
        "region_risk",
        "request_frequency",
        "possibility_of_fraud"
    ])

    return pd.concat([df.iloc[:, :10].reset_index(drop = True), enrichment], axis = 1)