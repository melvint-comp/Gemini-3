import tensorflow as tf
from tensorflow.keras import layers, models, Input

def build_security_enrichment_model(input_dim):
    inputs = Input(shape = (input_dim,))
    x = layers.BatchNormalization()(inputs)

    x = layers.Dense(128, activation = "relu")(x)
    x = layers.Dropout(0.3)(x)

    x = layers.Dense(64, activation = "relu")(x)
    shared = layers.Dense(64, activation="relu")(x)

    def head(name):
        return layers.Dense(1, activation = "sigmoid", name=name)(
            layers.Dense(32, activation = "relu")(shared)
        )

    identity = head("identity_mismatch")
    unusual = head("unusual_time")
    region = head("region_risk")
    freq = head("request_frequency")

    combined = layers.Concatenate()([identity, unusual, region, freq, shared])
    fraud = layers.Dense(1, activation = "sigmoid", name="possibility_of_fraud")(
        layers.Dense(32, activation = "relu")(combined)
    )

    model = models.Model(inputs, [identity, unusual, region, freq, fraud])

    model.compile(
        optimizer = tf.keras.optimizers.Adam(0.0003),
        loss = "binary_crossentropy",
        metrics = ["accuracy"]
    )

    return model