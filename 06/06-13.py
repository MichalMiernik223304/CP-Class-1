array1 = [1, 2, 3, 4, 5]
array2 = []

for i in range (0, len(array1)-1):
    array2.insert(i, array1[i]**2)

print(f"Array: {array1}")
print(f"Second power: {array2}")