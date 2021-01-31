from ..common.constants import MODEL_DEEPGO, MODEL_DEEPRED, MODEL_GOLABELER, MODEL_XBERT
from .DeepGoPlusTokenizer import DeepGoPlusTokenizer

TOKENIZER = {
    MODEL_DEEPGO: DeepGoPlusTokenizer(),
    # etc.
}