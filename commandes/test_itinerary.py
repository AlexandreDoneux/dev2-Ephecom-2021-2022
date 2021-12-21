import unittest
from commandes import itinerary
from commandes.itinerary import Itinerary


class TestItinerary(unittest.TestCase):
    def test_itinerary_is_instance(self):
        itin = Itinerary('Alfons Moerenhoutstraat 80, Overijse', 'Rue Saint Michel 37, Bruxelles')
        itin1 = Itinerary('ggfgfgfgfgfg', 'fhbfhbfhbfhbfhfh')
        itin2 = Itinerary(5555, 'hbfhfhbdhb')
        self.assertIsInstance(itin,Itinerary)
        self.assertIsInstance(itin1, Itinerary)
        self.assertIsInstance(itin2, Itinerary)
    def test_show_itinerary(self):
        self.assertTrue(itinerary.Itinerary('Wavre', 'Louvain').show_itinerary())
        self.assertEqual(itinerary.Itinerary('ggfgfgfgfgfg', 'fhbfhbfhbfhbfhfh').show_itinerary(), 'NOT_FOUND')
        self.assertEqual(itinerary.Itinerary('Togo', 'Rue Saint Michel 37, Bruxelles').show_itinerary(), 'ZERO_RESULTS')
if __name__ == '__main__':
    unittest.main()