import tensorflow as tf

model = tf.keras.models.load_model("kc_ids_model.h5")

def detect(features):
    score = model.predict([features])[0][0]
    return score