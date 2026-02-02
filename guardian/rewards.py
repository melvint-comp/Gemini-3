def calculate_reward(event, detection):
    """
    Compares detection result with ground truth authorization.
    Returns an outcome and reward score.
    """

    actual_unauthorized = not event["authorized"]
    predicted_suspicious = detection["suspicious"]

    if predicted_suspicious and actual_unauthorized:
        outcome = "true_positive"
        reward = 1.0
    elif predicted_suspicious and not actual_unauthorized:
        outcome = "false_positive"
        reward = -0.5
    elif not predicted_suspicious and not actual_unauthorized:
        outcome = "true_negative"
        reward = 0.5
    else:
        outcome = "false_negative"
        reward = -1.0

    return {
        "outcome": outcome,
        "reward": reward
    }


if __name__ == "__main__":
    # Local test
    sample_event = {
        "authorized": False
    }

    sample_detection = {
        "suspicious": True
    }

    result = calculate_reward(sample_event, sample_detection)

    print("Reward Evaluation:")
    for key, value in result.items():
        print(f"{key}: {value}")

