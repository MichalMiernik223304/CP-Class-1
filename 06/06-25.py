def minmax(array):
    n = len(array)
    array2=[]
    while n > 1:
        for i in range(0, len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
        n = n - 1
    array2.append(array[0])
    array2.append(array[-1])

    return array2


array = [4, 2, 8, 4, 7, 9, 5]
array2 = minmax(array)
print(f"Array: {array}")
print(f"Result: {array2}")