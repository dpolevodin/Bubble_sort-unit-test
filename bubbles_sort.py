def bubbles_sort(arr):
    len_arr = len(arr) # для получения кол-ва проходов по всему массиву
    for i in range(len_arr-1):
        for j in range(len_arr-i-1): # проходы без последнего проверяемого элемента
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
