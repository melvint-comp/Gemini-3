import pandas as pd
import numpy as np

def synthesize_cloud_csv(num_rows = 1000):
    rows = []

    for _ in range(num_rows):

        profile = np.random.choice(["normal", "automated", "attacker"], p = [0.7, 0.15, 0.15])

        hour = np.random.randint(0, 24)
        day = np.random.randint(0, 7)

        if profile == "normal":
            region = np.random.choice([0, 1], p=[0.8, 0.2])
            ip_risk = np.random.beta(2, 10)
            req_5m = np.random.poisson(2)
            req_1h = np.random.poisson(12)
            failed_ratio = np.random.beta(1, 15)
            key_sens = np.random.uniform(0.2, 0.6)
            hist_access = np.random.beta(5, 2)
            principal = np.random.choice([0, 1], p=[0.8, 0.2])
            fraud = 0

        elif profile == "automated":
            region = np.random.choice([0, 2])
            ip_risk = np.random.beta(2, 4)
            req_5m = np.random.poisson(8)
            req_1h = np.random.poisson(60)
            failed_ratio = np.random.beta(1, 5)
            key_sens = np.random.uniform(0.4, 0.7)
            hist_access = np.random.beta(6, 1)
            principal = 2
            fraud = 0

        else:
            region = np.random.choice([3, 4])
            ip_risk = np.random.beta(8, 1)
            req_5m = np.random.poisson(20)
            req_1h = np.random.poisson(120)
            failed_ratio = np.random.beta(5, 1)
            key_sens = np.random.uniform(0.7, 1.0)
            hist_access = np.random.beta(1, 6)
            principal = np.random.choice([0, 1])
            hour = np.random.choice([0,1,2,3,4,22,23])
            fraud = 1

        identity = 1 if region >= 3 else 0
        unusual = 1 if hour in [0,1,2,3,4,22,23] else 0
        region_risk = 1 if region >= 3 else 0
        freq = 1 if req_5m > 10 else 0

        rows.append([
            hour, 
            day, 
            region, 
            ip_risk, 
            req_5m,
            req_1h, 
            principal,
            key_sens, 
            hist_access, 
            failed_ratio,
            identity, 
            unusual, 
            region_risk, 
            freq, 
            fraud
        ])

    return pd.DataFrame(rows, columns=[
        "hour_of_day",
        "day_of_week",
        "region_code",
        "source_ip_risk",
        "request_count_5m",
        "request_count_1h",
        "principal_type",
        "key_sensitivity",
        "historical_access_rate",
        "failed_auth_ratio",
        "identity_mismatch",
        "unusual_time",
        "region_risk",
        "request_frequency",
        "possibility_of_fraud"
    ])