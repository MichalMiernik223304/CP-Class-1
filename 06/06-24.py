array = [5, 19, 2, 5, 6, 30, 50, 0]
array_greater = []

number = int(input("Enter number: "))
for i in array:
    if i > number:
        array_greater.append(i)

print(f"Numbers from array greater than {number}: {array_greater}")