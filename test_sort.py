import unittest
from bubbles_sort import bubbles_sort


class TestBubblesSort(unittest.TestCase):
    def test_bubbles_sort(self):
        """
        Test that array sorting correctly
        """
        data_test = [0, 1, 3, 5, 22, 33, 59, 121]
        result = bubbles_sort([3, 0, 1, 33, 22, 5, 121, 59])
        self.assertEqual(result,data_test)
        
if __name__ == '__main__':
    unittest.main()
