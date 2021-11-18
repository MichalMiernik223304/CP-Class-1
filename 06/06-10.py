def sum(array):
    suma = 0
    for i in array:
        suma = suma + i
    return suma

def array2str(array):
    st = ""

    for i in array:
        st = st + str(i) + " "
    print(f"Array: {st}")

array1 = [1, 2, 3, 4]

array2str(array1)
x = sum(array1)
print(f"Sum of values: {x}")

