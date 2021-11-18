array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
array_even = []
array_odd = []

for i in array:
    if i % 2 == 0:
        array_even.append(i)
    else:
        array_odd.append(i)

print(f"Even numbers: {array_even}")
print(f"Odd numbers: {array_odd}")