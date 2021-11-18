def reverse(array):
    array2 = []
    for i in range(0, int(len(array)), 1):
        array2.insert(i, array[int(len(array)) - 1 - i])

    print(array2)

array1 = [15, 8, 31, 47, 2, 19]
reverse(array1)

