from .Tokenizer import Tokenizer

import logging
logger = logging.getLogger(__name__)


class IdentityTokenizer(Tokenizer):

    def tokenize(self, sequence):
        return sequence
