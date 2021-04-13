
from tensorflow import keras
from transformers import AutoModel 
import zipfile
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


def load_model_transformer(path: str):
    """
        Load a Pytorch at a given path

        https://pytorch.org/tutorials/beginner/saving_loading_models.html

        :param path: Path to model to load
        :return: Pytorch model
    """
    unzip_path = path.replace(".zip", "")
    with zipfile.ZipFile(path, 'r') as zip_ref:
        zip_ref.extractall(unzip_path)
    model = AutoModel.from_pretrained(unzip_path)
    model.eval()
    return model



