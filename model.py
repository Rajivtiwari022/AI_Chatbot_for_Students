from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout


def build_model(input_size, output_size):

    model = Sequential()

    model.add(Dense(128, activation="relu", input_shape=(input_size,)))
    model.add(Dropout(0.3))

    model.add(Dense(64, activation="relu"))
    model.add(Dropout(0.3))

    model.add(Dense(output_size, activation="softmax"))

    model.compile(
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"]
    )

<<<<<<< HEAD
    return model
=======
    return model
>>>>>>> 39d268a86529baf6297ae635c38359e48839e4b9
