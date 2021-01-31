from ..common.constants import MODEL_DEEPGO, MODEL_DEEPRED, MODEL_GOLABELER, MODEL_XBERT
from .DeepGoPostProcess import DeepGoPostProcess
from .PostProcess import PostProcess

import pandas as pd
import logging

logger = logging.getLogger(__name__)


def get_deepgo_postproces() -> PostProcess:

    terms_df = pd.read_pickle("resources/terms.pkl")
    return DeepGoPostProcess(terms_df)


POSTPROCESS = {
    MODEL_DEEPGO: get_deepgo_postproces(),
    # etc.
}


def get_postprocess(model_name: str) -> PostProcess:

    if model_name in POSTPROCESS:
        logger.info(f'Loading post-process {POSTPROCESS[model_name]}')
        return POSTPROCESS[model_name]
    else:
        logger.warning(f'No model name {model_name} - default post-processor loaded')
        return PostProcess()
