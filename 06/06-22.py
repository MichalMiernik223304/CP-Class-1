def bubblesort(array):
    n = len(array)
    while n > 1:
        for i in range(0, len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
        n = n - 1
    print(array)
    return array

array = [5, 1, 9, 6, 1]
bubblesort(array)
dif = array[-1] - array[1]
print(f"Array: {array}")
print(f"Difference between the largest and smallest value: {dif}")