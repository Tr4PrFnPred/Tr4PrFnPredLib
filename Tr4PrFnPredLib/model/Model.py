from ..common.constants import MODEL_DEEPGO, MODEL_DEEPRED, MODEL_GOLABELER, MODEL_XBERT, MODEL_PROTBERT
from tensorflow import keras
import torch.nn as nn
from typing import Union


class Model:
    """
        Class to encapsulate a model and perform model operations

    """

    def __init__(self, model_name:str, model):
        self.model_name = model_name

        if isinstance(model, keras.Model):
            self.model = model
        elif isinstance(model, nn.Module):
            self.model = model
        else:
            raise ValueError("Invalid type for model argument:", type(model))

    def predict(self, data: Union[str, list]):

        # TODO: predict function that changes behavior based on platform

        if self.model_name == MODEL_DEEPGO:
            return self.model.predict(data)
        elif self.model_name == MODEL_PROTBERT:
            outputs = []
            for sample in data:
                output = model(sample["input_ids"], token_type_ids=sample["token_type_ids"], attention_mask=sample["attention_mask"])
                output.append(outputs)
            return outputs
        else:
            return []
