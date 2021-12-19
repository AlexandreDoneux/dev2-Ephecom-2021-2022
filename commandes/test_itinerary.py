import unittest
from commandes import itinerary
from commandes.itinerary import Itinerary


class TestItinerary(unittest.TestCase):
    def test_itinerary_is_instance(self):
        itin = Itinerary()
        itin1 = Itinerary("Les routes")
        itin2 = Itinerary(5555)
        self.assertIsInstance(itin,Itinerary)
        self.assertIsInstance(itin1, Itinerary)
        self.assertIsInstance(itin2, Itinerary)
    def test_show_itinerary(self):
        self.assertTrue(itinerary.Itinerary().show_itinerary())
if __name__ == '__main__':
    unittest.main()