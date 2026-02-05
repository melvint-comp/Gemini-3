def critique(metrics):
    return f"""
    Accuracy: {metrics['accuracy']}
    False positives observed.
    Suggest threshold tuning or additional temporal features.
    """
