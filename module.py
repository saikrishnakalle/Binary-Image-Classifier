from tensorflow.keras.models import model_from_json
from tensorflow.keras.utils import img_to_array

import cv2
import numpy as np

with open("model/res.json", "r") as f:
    model = model_from_json(f.read())

model.load_weights("model/res.h5")


def predict_image(path):

    img = cv2.imread(path)

    img = cv2.resize(img, (200, 200))

    img = img_to_array(img)

    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img, verbose=0)[0]

    return np.argmax(prediction)


def check(file1, file2):

    pred1 = predict_image(file1)
    pred2 = predict_image(file2)

    if pred1 == 0 and pred2 == 0:
        return "two", "photos"

    elif pred1 == 1 and pred2 == 1:
        return "two", "signatures"

    elif pred1 == 1 and pred2 == 0:
        return file2, file1

    else:
        return file1, file2
