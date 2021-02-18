import unittest
from bubbles_merge_sort import MostSortMethods

test1 = MostSortMethods()

class MostSortMethods(unittest.TestCase):
  
    def test_bubbles_sort(self):
        """
        Test that array sorting correctly
        """
        data_test = [0, 1, 3, 5, 22, 33, 59, 121]
        result = test1.bubbles_sort([3, 0, 1, 33, 22, 5, 121, 59])
        
        data_test2 = []
        result2 = test1.bubbles_sort([])
        
        data_test3 = [0,1]
        result3 = test1.bubbles_sort([1,0])
        
        self.assertEqual(result,data_test, 'неправильная сортировка')
        self.assertEqual(result2,data_test2, 'Проблемы с пустым списком')
        self.assertEqual(result3,data_test3, 'Проблема с 0')
        
    def test_merge_sort(self):
        """
        Test that array sorting correctly
        """
        data_test4 = [0, 1, 3, 5, 22]
        result4 = test1.merge_sort([0, 22, 5, 3, 1])
        
        data_test5 = [0, 1, 3, 5]
        result5 = test1.merge_sort([0, 3, 5, 1])
        
        data_test6 = [1,2]
        result6 = test1.merge_sort([2,1])
                  
        self.assertEqual(result4,data_test4, 'неправильная сортировка')
        self.assertEqual(result5,data_test5, 'Проблемы с пустым списком')
        self.assertEqual(result6,data_test6, 'Проблема с массивом из двух чисел')

if __name__ == '__main__':
    unittest.main()
