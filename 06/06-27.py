def tostr(array):
    print(f"Array: {array}")
    print(f"String:", end=" ")
    print(*array, sep=", ")

array = [5,4,3,2,6,5]
tostr(array)