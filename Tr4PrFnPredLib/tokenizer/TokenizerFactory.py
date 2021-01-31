from .Tokenizer import Tokenizer
from .IdentityTokenizer import IdentityTokenizer
from .tokenizer_config import TOKENIZER

import logging

logger = logging.getLogger(__name__)


def get_tokenizer(model_name: str) -> Tokenizer:

    if model_name in TOKENIZER:
        logger.info(f'Loading tokenizer {TOKENIZER[model_name]}')
        return TOKENIZER[model_name]
    else:
        logger.warning(f'No model name {model_name} - default tokenizer loaded')
        return IdentityTokenizer()