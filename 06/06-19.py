array1 = [2, 3, 2, 5, 8, 1, 9, 8]
array2 = []
counter = 0

for i in range(0, len(array1)-1):
    for j in range(0, i):
        if array1[i] == array1[j]:
            counter = counter + 1
    for j in range(i+1, len(array1)-1):
        if array1[i] == array1[j]:
            counter = counter + 1

    if counter == 0:
        array2.append(array1[i])
    counter = 0

print(array2)