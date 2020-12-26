from typing import Union, Optional

from .model.Model import Model
from .model_loader.ModelLoader import ModelLoader
from .model_loader.ModelLoaderLocal import ModelLoaderLocal
from .tokenizer.Tokenizer import Tokenizer
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
        tokenized = self.tokenizer.tokenize(data)
        prediction = self.model.predict(tokenized)

        return prediction


def pipeline(
    model: Union[str, Model],
    tokenizer: Optional[Union[str, Tokenizer]] = IdentityTokenizer(),
    model_loader: Optional[ModelLoader] = ModelLoaderLocal(".")
) -> Pipeline:

    if isinstance(model, str):
        # load the model with the model_loader class
        logging.debug(f"Loading model: {model}")
        model = Model(model_loader.load_model(model))
    elif not isinstance(model, Model):
        # if it's not a Model class, then its an invalid argument
        raise TypeError("Invalid argument passed for model: " + model)

    if isinstance(tokenizer, str):
        pass
    elif not isinstance(tokenizer, Tokenizer):
        raise TypeError("Invalid argument passed for tokenizer: " + tokenizer)

    return Pipeline(model, tokenizer)
