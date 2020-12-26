
from tensorflow import keras
import torch

"""
    Platform specific model load functions

"""


def load_model_keras(path: str):
    """
        Load a keras model at a given path

        :param path: Path to model to load
        :return: Keras model
    """

    return keras.models.load_model(path)


def load_model_pytorch(path: str):
    """
        Load a Pytorch at a given path

        https://pytorch.org/tutorials/beginner/saving_loading_models.html

        :param path: Path to model to load
        :return: Pytorch model
    """
    model = torch.load(path)
    model.eval()
    return model



