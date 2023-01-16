import os
from PIL import Image, ImageDraw as D
import tensorflow as tf
import numpy as np

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.image import ImageDataGenerator

image_size = (32, 32)

class Classifier:


    def __init__(self, model_name='Code/model_utils/models/model_v1.h5'):
        self.__model = keras.models.load_model(model_name)


    def predict_image(self, image):
        saved_image = image.copy()
        image = np.asarray(image.resize((800, 500)))
        image = image.reshape((500, 800, 3))
        x_size, y_size = image_size
        crops = [(  (x, y), 
                    (x + x_size, y + y_size), 
                    image[x:x+x_size, y:y+y_size] / 255) for x in range(0, image.shape[0], x_size) for y in range(0,image.shape[1], y_size)]
        predictions = self.__model.predict(np.array([crop[-1] for crop in crops if crop[-1].shape == (*image_size, 3)]))
        future_rectangles = [(start, end, prediciton, prediciton.argmax()) for (start, end, _), prediciton in zip(crops, predictions)]
        draw = D.Draw(saved_image)
        types = ["cold", "occluded", "warm", "white"]
        rect = {"warm": [],
                "cold": [],
                "white": []}
        o = {"warm": "red",
            "cold": "blue",
            "white": "purple",
            "occluded": "green"
        }
        for (x, y), (x1, y1), pred, tp in future_rectangles:
            if tp != 3:
                draw.rectangle([(y, x), (y1, x1)], outline=o[types[tp]], width=2)
                draw.text((y, x), '.', fill="green", align="center")
        return saved_image
