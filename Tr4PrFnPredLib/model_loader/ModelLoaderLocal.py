import os
import logging

from .ModelLoader import ModelLoader
from .ModelLoaderUtil import load_model_keras, load_model_pytorch
from .model_config import MODEL_FILE

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

        if model_name in MODEL_FILE:
            logger.info("Loading model: " + model_name)
            model_file = MODEL_FILE[model_name]
            model = load_model_keras(os.path.join(self.model_dir, model_file))
            return model
        else:
            logger.warning("No model found with name: " + model_name)
            return None
