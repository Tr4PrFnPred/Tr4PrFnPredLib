from .ModelLoader import ModelLoader


class ModelLoaderImpl(ModelLoader):

    def __init__(self):
        pass

    def load_model(self, model_name):
        """
            TODO: Implement in the future
            Idea is to have a cloud service that stores all models. This function will
            look for the model specified by the parameter model_name to download/load model.

            Currently use ModelLoaderLocal class.

            :param model_name: name of the model to download and load
            :return: the found model
        """

        pass
