import unittest
from bubbles_sort import bubbles_sort


class TestBubblesSort(unittest.TestCase):
    def test_bubbles_sort(self):
        """
        Test that array sorting correctly
        """
        data_test = [0, 1, 3, 5, 22, 33, 59, 121]
        result = bubbles_sort([3, 0, 1, 33, 22, 5, 121, 59])
        
        data_test2 = []
        result2 = bubbles_sort([])
        
        data_test3 = [0]
        result3 = bubbles_sort([0])
        
        self.assertEqual(result,data_test, 'неправильная сортировка')
        self.assertEqual(result2,data_test2, 'Проблемы с пустым списком')
        self.assertEqual(result3,data_test3, 'Сортировка работает корректно')

if __name__ == '__main__':
    unittest.main()
