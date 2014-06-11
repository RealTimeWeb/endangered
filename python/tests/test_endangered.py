import unittest
from python.src import endangered


class TestEndangeredDatabase(unittest.TestCase):

    def test_get_endangered_info(self):
        endangered.connect()

        keys = ['Amphibians', 'Birds', 'Country', 'Fishes', 'ISO country code',
                'Mammals', 'Mollusks', 'Other Inverts', 'Plants', 'Reptiles',
                'Total']

        endangered_info = endangered.get_endangeredSpecies_information(
            "Country==Afghanistan")
        self.assertTrue(isinstance(endangered_info, list))

        for dict_item in endangered_info:

            intersection = set(keys).intersection(dict_item)
            self.assertEqual(11, len(intersection))