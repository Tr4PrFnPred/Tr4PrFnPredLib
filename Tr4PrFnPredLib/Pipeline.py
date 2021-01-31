from typing import Union, Optional

from .model.Model import Model
from .model_loader.ModelLoader import ModelLoader
from .model_loader.ModelLoaderLocal import ModelLoaderLocal
from .tokenizer.Tokenizer import Tokenizer
from .tokenizer.TokenizerFactory import get_tokenizer
from .tokenizer.IdentityTokenizer import IdentityTokenizer


import logging
logger = logging.getLogger(__name__)


class Pipeline:

    def __init__(self,
                 model: Model,
                 tokenizer: Tokenizer):
        """
            Create a pipeline

            :param model: Pre-trained model used for inference
            :param tokenizer: Pre-trained tokenizer to tokenize sentence
        """

        self.model = model
        self.tokenizer = tokenizer

    def predict(self, data: Union[str, list]):
        logger.info(data)

        if isinstance(data, str):
            # expect a csv formatted string for multiple sequences
            # or a single string for a single sequence
            data = data.split(",")

        tokenized = self.tokenizer.tokenize(data)
        prediction = self.model.predict(tokenized)

        return prediction


def pipeline(
    model_name: Union[str, Model],
    tokenizer: Optional[Union[str, Tokenizer]] = None,
    model_loader: Optional[ModelLoader] = ModelLoaderLocal(".")
) -> Pipeline:

    if isinstance(model_name, str):
        # load the model with the model_loader class
        logging.debug(f"Loading model: {model_name}")
        model = Model(model_loader.load_model(model_name))
        tokenizer = get_tokenizer(model_name)
    elif not isinstance(model_name, Model):
        # if it's not a Model class, then its an invalid argument
        raise TypeError("Invalid argument passed for model: " + model_name)

    if isinstance(tokenizer, Tokenizer):
        tokenizer = get_tokenizer(model_name)

    return Pipeline(model, tokenizer)
