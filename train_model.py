import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense

train_dir = "dataset/train"

model = Sequential()

model.add(
    Conv2D(
        32,
        (3, 3),
        activation="relu",
        input_shape=(200, 200, 3)
    )
)

model.add(MaxPooling2D())

model.add(Conv2D(64, (3, 3), activation="relu"))
model.add(MaxPooling2D())

model.add(Flatten())

model.add(Dense(128, activation="relu"))

model.add(Dense(2, activation="softmax"))

model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

print(model.summary())

model.save("model/res.h5")
