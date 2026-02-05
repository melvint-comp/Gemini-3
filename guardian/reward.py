def reward(prediction, actual):
    if prediction > 0.7 and actual == 1:
        return +1
    if prediction < 0.3 and actual == 0:
        return +0.5
    return -1