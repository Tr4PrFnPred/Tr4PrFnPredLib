import unittest

from Tr4PrFnPredLib.postprocess.PostProcessFactory import get_postprocess
from Tr4PrFnPredLib.postprocess.DeepGoPostProcess import DeepGoPostProcess


class TestPostProcess(unittest.TestCase):

    def test_deepgoplus_postprocess(self):

        postprocess = get_postprocess("deepgoplus")
        self.assertTrue(isinstance(postprocess, DeepGoPostProcess))