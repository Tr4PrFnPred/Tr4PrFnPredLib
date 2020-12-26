from tensorflow import keras
from typing import Union


class Model:
    """
        Class to encapsulate a model and perform model operations

    """

    def __init__(self, model):

        if isinstance(model, keras.Model):
            self.model = model
        else:
            raise ValueError("Invalid type for model argument:", type(model))

    def predict(self, data: Union[str, list]):

        # TODO: predict function that changes behavior based on platform

        if isinstance(self.model, keras.Model):
            return self.model.predict(data)
        else:
            return []
