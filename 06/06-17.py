array1 = [4, 36, 12, 28, 9, 44, 5]
array2 = [5, 1, 36]
array3 = []


for i in range(0, len(array1)):
    x = False
    for j in range(0, len(array2)):
        if array1[i] == array2[j]:
            x = True
            break
    if x == False:
        array3.append(array1[i])

print(array3)