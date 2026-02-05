import numpy as np
from model import build_model

def train(X, y):
    model = build_model(X.shape[1])
    model.fit(X, y, epochs = 10, batch_size = 32)
    model.save("kc_ids_model.h5")