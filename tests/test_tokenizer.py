import unittest

from Tr4PrFnPredLib.tokenizer.TokenizerFactory import get_tokenizer
from Tr4PrFnPredLib.tokenizer.DeepGoPlusTokenizer import DeepGoPlusTokenizer
from Tr4PrFnPredLib.tokenizer.IdentityTokenizer import IdentityTokenizer


class TestTokenizer(unittest.TestCase):

    def test_get_deepgoplus_tokenizer(self):

        tokenizer = get_tokenizer("deepgoplus")
        self.assertTrue(isinstance(tokenizer, DeepGoPlusTokenizer))

    def test_invalid_tokenizer(self):
        
        tokenizer = get_tokenizer("Invalid")
        self.assertTrue(isinstance(tokenizer, IdentityTokenizer))
