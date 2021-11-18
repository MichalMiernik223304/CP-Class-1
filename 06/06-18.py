array1 = [5, 16, 8]
array2 = [28, 88, 8, 75, 0, -1, 63]
array3 = [15, 1, 12, 19, 63]

def bubblesort(array):
    n = len(array)
    while n > 1:
        for i in range(0, len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
        n = n - 1
    print(array)


bubblesort(array2)