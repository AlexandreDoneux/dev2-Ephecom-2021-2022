# python 3.10
# UTF-8
import unittest
import api_end_point


class TestItinerary(unittest.TestCase):
    def test_show_itinerary(self):
        self.assertTrue(api_end_point.Itinerary().show_itinerary())
if __name__ == '__main__':
    unittest.main()