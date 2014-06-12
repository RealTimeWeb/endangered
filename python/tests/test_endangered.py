import unittest
from python.src import endangered


class TestEndangeredDatabase(unittest.TestCase):

    def test_get_endangered_info(self):
        endangered.connect()

        keys = ['amphibians', 'birds', 'country', 'fishes', 'iso',
                'mammals', 'mollusks', 'other', 'plants', 'reptiles',
                'total']

        endangered_info = endangered.get_endangeredSpecies_information(
            "Country==Afghanistan")
        self.assertTrue(isinstance(endangered_info, dict))

        intersection = set(keys).intersection(endangered_info)
        self.assertEqual(11, len(intersection))