from .ModelLoader import ModelLoader
from tensorflow import keras


class ModelLoaderMock(ModelLoader):

    def load_model(self, model_name):
        return keras.Model()
