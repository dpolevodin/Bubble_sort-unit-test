# -*- coding: utf-8 -*-
"""
@author: polevodin-di
"""
class MostSortMethods():
    """
    most popular function for sorting
    """

    def bubbles_sort(self, arr):
        len_arr = len(arr)
        for i in range(len_arr-1):
            for j in range(len_arr-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr
    
    def merge_sort(self, arr):
    
        if len(arr) > 1:
            arr_mid = len(arr) // 2
            arr1 = arr[arr_mid:]
            arr2 = arr[:arr_mid]
            
            self.merge_sort(arr1)
            self.merge_sort(arr2)
    
            i, j, k = 0, 0, 0
            while i < len(arr1) and j < len(arr2):
                if arr2[j] > arr1[i]:
                    arr[k] = arr1[i]
                    i += 1
                else:
                    arr[k] = arr2[j]
                    j += 1
                k += 1
                
                
            while i < len(arr1):
                arr[k] = arr1[i]
                i += 1
                k += 1
            
            while j < len(arr2):
                arr[k] = arr2[j]
                j += 1
                k += 1
        return arr
