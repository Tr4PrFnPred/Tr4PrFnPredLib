from abc import ABC, abstractmethod


class ModelLoader(ABC):

    @abstractmethod
    def load_model(self, model_name):
        """
            Load a model based the name specified.

            TODO: Need to consider the different platforms - e.g., Keras, tensorflow, pytorch, etc.
        :return:
        """
        pass
