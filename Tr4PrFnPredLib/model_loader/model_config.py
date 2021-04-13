from ..common.constants import MODEL_DEEPGO, MODEL_DEEPRED, MODEL_GOLABELER, MODEL_XBERT, MODEL_PROTBERT
from .ModelLoaderUtil import load_model_keras, load_model_transformer

"""
    Name of model files if loading them locally.
"""
MODEL_FILE = {
    MODEL_DEEPGO: "deepgoplus.h5",
    MODEL_PROTBERT: "test0.pth.zip",
    # etc.
}


"""
    URLS for models hosted on github.
"""
MODEL_URLS = {
    MODEL_DEEPGO: "https://github.com/Tr4PrFnPred/Tr4PrFnPredLib/releases/download/v0.0.1/deepgoplus.h5",
    MODEL_PROTBERT: "https://github.com/Tr4PrFnPred/Tr4PrFnPredLib/releases/download/v0.0.2/test0.pth.zip"
    # etc.
}

"""
    Model loaders
"""
MODEL_LOADER = {
            MODEL_DEEPGO: load_model_keras, 
            MODEL_PROTBERT: load_model_transformer
        } 