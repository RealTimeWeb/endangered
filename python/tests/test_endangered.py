import unittest
from python.src import endangered


class TestEndangeredDatabase(unittest.TestCase):

    def test_get_endangered_info(self):
        endangered.connect()
        endangered._start_editing()

        keys = ['amphibians', 'birds', 'country', 'fishes', 'iso',
                'mammals', 'mollusks', 'other', 'plants', 'reptiles',
                'total']

        endangered_info = endangered.get_endangeredSpecies_information(
            "Country==Afghanistan")
        endangered._save_cache()
        self.assertTrue(isinstance(endangered_info, dict))

        intersection = set(keys).intersection(endangered_info)
        self.assertEqual(11, len(intersection))


    def test_get_endangered_offline(self):
        endangered.disconnect("cache.json")

        keys = ['amphibians', 'birds', 'country', 'fishes', 'iso',
                'mammals', 'mollusks', 'other', 'plants', 'reptiles',
                'total']

        endangered_info = endangered.get_endangeredSpecies_information(
            "Country==Afghanistan")
        self.assertTrue(isinstance(endangered_info, dict))

        intersection = set(keys).intersection(endangered_info)
        self.assertEqual(11, len(intersection))
