import unittest
from commandes import api_end_point


class TestItinerary(unittest.TestCase):
    def test_show_itinerary(self):
        self.assertTrue(api_end_point.Itinerary().show_itinerary())
if __name__ == '__main__':
    unittest.main()