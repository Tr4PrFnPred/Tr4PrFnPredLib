from ..common.constants import MODEL_DEEPGO, MODEL_DEEPRED, MODEL_GOLABELER, MODEL_XBERT, MODEL_PROTBERT
from .DeepGoPlusTokenizer import DeepGoPlusTokenizer
from .ProtBERTTokenizer import ProtBERTTokenizer

TOKENIZER = {
    MODEL_DEEPGO: DeepGoPlusTokenizer(),
    MODEL_PROTBERT: ProtBERTTokenizer()
    # etc.
}