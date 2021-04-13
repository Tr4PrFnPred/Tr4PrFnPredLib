from ..common.constants import MODEL_DEEPGO, MODEL_DEEPRED, MODEL_GOLABELER, MODEL_XBERT, MODEL_PROTBERT
from .ModelLoader import ModelLoader
from .model_config import MODEL_URLS, MODEL_FILE, MODEL_LOADER

import requests
import logging
import os
from pathlib import Path

logging.basicConfig(level = logging.INFO)
logger = logging.getLogger(__file__)



class ModelRequests:

    def __init__(self, model_config=MODEL_URLS):
        self.model_config = model_config

    def get_model(self, model_name: str, model_path: str):
        model_url = self.model_config[model_name]
        model_request = requests.get(model_url, allow_redirects=True)

        with open(model_path, "wb") as model:
            model.write(model_request.content)

        logger.info(f'Finished downloading model from ${model_url}')


class ModelLoaderRelease(ModelLoader):

    def __init__(self, model_dir: str, model_requester=ModelRequests()):
        """
            Create a Model Loader class.

            :param model_dir: Absolute path of the model directory.
        """
        self.model_dir = model_dir
        self.model_requester = model_requester

    def load_model(self, model_name: str):
        """
            Load model hosted on Github releases.

            :param model_name: name of the model to download and load
            :return: The loaded model.
        """

        logger.info(f'Loading model name: ${model_name}')

        model_file_name = MODEL_FILE[model_name]

        model_path = Path(self.model_dir) / model_file_name

        logger.info(f'Checking if model exists')
        if Path.exists(Path(self.model_dir)):

            if Path.exists(model_path):
                logger.info(f'Found existing ${model_name} model')
                return load_model_keras(str(model_path))
        else:
            logger.info(f'Creating model directory')
            os.makedirs(self.model_dir)

        self.model_requester.get_model(model_name, model_path)
        
        

        return MODEL_LOADER[model_name](model_path)
