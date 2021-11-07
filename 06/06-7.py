array = [1, 2, 3, 4, 5, 6, 7]
odd = 0
even = 0

for i in range(0, len(array)):
    if array[i]%2 == 0:
        even += 1
    else:
        odd += 1
        
print(f"Odd numbers: {odd}")
print(f"Even numbers: {even}")