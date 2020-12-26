import os
import logging

from tensorflow import keras

from .ModelLoader import ModelLoader

logger = logging.getLogger(__name__)


class ModelLoaderLocal(ModelLoader):
    """
        Initial model loader which tries to find all pre-trained models on disk with a specified
        directory.
    """

    def __init__(self, model_dir):
        self.model_dir = model_dir

    def load_model(self, model_name):

        # TODO: different libraries - e.g. keras loader, pytorch loader, etc.

        if model_name in os.listdir(self.model_dir):
            logger.info("Loading model: " + model_name)
            return keras.models.load_model(os.path.join(self.model_dir, model_name))
        else:
            logger.warning("No model found with name: " + model_name)
            return None
