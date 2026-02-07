def train_model(model, X, y):
    model.fit(X, y, epochs = 12, batch_size = 64, validation_split = 0.2, verbose = 1)