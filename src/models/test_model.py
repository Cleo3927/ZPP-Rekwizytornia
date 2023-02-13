from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt


class Model():
    def __init__(self):
        self.conv_base = keras.applications.vgg16.VGG16(
            weights="imagenet", include_top=False)
        self.conv_base.trainable = False

    def train(self):
        data_augmentation = keras.Sequential(
            [
                layers.RandomFlip("horizontal"),
                layers.RandomRotation(0.1),
                layers.RandomZoom(0.2),
            ]
        )
        inputs = keras.Input(shape=(180, 180, 3))
        x = data_augmentation(inputs)
        x = keras.applications.vgg16.preprocess_input(x)
        x = conv_base(x)
        x = layers.Flatten()(x)
        x = layers.Dense(256)(x)
        x = layers.Dropout(0.5)(x)
        outputs = layers.Dense(1, activation="sigmoid")(x)
        self.model = keras.Model(inputs, outputs)
        self.model.compile(loss="binary_crossentropy",
            optimizer="rmsprop", metrics=["accuracy"])

    def answer(self, photo_name):
        return photo_name


model = Model()