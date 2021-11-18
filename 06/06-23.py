def bubblesort(array):
    n = len(array)
    while n > 1:
        for i in range(0, len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
        n = n - 1
    return array

def median(array):
    if len(array) % 2 ==0:
        med = (array[int(len(array)/2 - 1)] + array[int(len(array)/2)]) / 2
    else:
        med = array[int(len(array)/2)]
    print(f"Array: {array}")
    print(f"Median of array: {med}")

array1 = [1, 0, 9, 4, 6, 9]
array2 = [6, 8, 3, 1, 0, 5, 7]

bubblesort(array1)
bubblesort(array2)

median(array1)
median(array2)