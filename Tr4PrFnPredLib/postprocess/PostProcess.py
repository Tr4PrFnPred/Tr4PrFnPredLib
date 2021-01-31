from abc import ABC, abstractmethod


class PostProcess(ABC):

    @abstractmethod
    def postprocess(self, predictions, **kwargs):
        return predictions
