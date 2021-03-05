import unittest
from Tr4PrFnPredLib.utils.ontology import Ontology


class TestUtils(unittest.TestCase):

    def test_ontology_file_load(self):

        ontology = Ontology()
        self.assertTrue(ontology.ont is not None)

