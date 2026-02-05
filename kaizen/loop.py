from guardian.detector import detect
from guardian.reward import reward

def kaizen_cycle(log, features, actual):
    score = detect(features)
    r = reward(score, actual)
    return score, r