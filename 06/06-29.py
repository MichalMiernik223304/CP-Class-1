array1 = [1, 2, 3, 4, 5, 6]
array2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 0
y = 0

for i in range(0, len(array1)):
    for j in range(0, len(array2)-1):
        if array1[i] == array2[j]:
            x = x + 1
        if x >= 1:
            y = y + 1
        x = 0

if y == len(array1):
    print(f"Array 1: {array1}")
    print(f"Array 2: {array2}")
    print("Array 1 is a subset of Array 2")
else:
    print(f"Array 1: {array1}")
    print(f"Array 2: {array2}")
    print("Array 1 is not a subset of Array 2")