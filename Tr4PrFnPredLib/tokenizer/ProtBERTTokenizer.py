from .Tokenizer import Tokenizer

import re
from transformers import BertTokenizer

import logging
logger = logging.getLogger(__name__)

PROTBERT_ORIGIN = "Rostlab/prot_bert"

class ProtBERTTokenizer(Tokenizer):
    def __init__(self, MAX_LEN=512):
        self.bert_tokenzer = BertTokenizer.from_pretrained(PROTBERT_ORIGIN, do_lower_case=False)
        self.MAX_LEN= MAX_LEN
        
    def tokenize(self, sequences):
        tokens = []
        for sequence in sequences:
            sequence = re.sub(r"[UZOB]", "X", sequence)
            inputs = self.bert_tokenzer.encode_plus(
                sequence,
                None,
                truncation=True,
                add_special_tokens=True,
                max_length=self.MAX_LEN,
                padding=True,
                return_token_type_ids=True
            )
            tokens.append(inputs)

        return tokens