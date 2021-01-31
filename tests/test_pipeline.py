import unittest

from Tr4PrFnPredLib.Pipeline import pipeline
from Tr4PrFnPredLib.tokenizer.DeepGoPlusTokenizer import DeepGoPlusTokenizer
from Tr4PrFnPredLib.model_loader.ModelLoaderMock import ModelLoaderMock
from Tr4PrFnPredLib.postprocess.DeepGoPostProcess import DeepGoPostProcess


class TestPipeline(unittest.TestCase):

    """
        Test the construction of a DeepGoPlus pipeline.
    """
    def test_deepgoplus_pipeline(self):

        test_pipeline = pipeline("deepgoplus", model_loader=ModelLoaderMock())

        self.assertTrue(isinstance(test_pipeline.tokenizer, DeepGoPlusTokenizer))
        self.assertTrue(isinstance(test_pipeline.post_process, DeepGoPostProcess))
