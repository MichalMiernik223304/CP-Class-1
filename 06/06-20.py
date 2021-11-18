def occurs(number, array):
    result = False
    for i in range(0, len(array)-1):
        if array[i] == number:
            result = True
            break
    return result


array = [15, 38, 7, 23, 14]
number = int(input("Enter number: "))

result = occurs(number, array)

print(f"Number: {number}")
print(f"Array: {array}")
if result == True:
    print(f"Number {number} appears in the array")
else:
    print(f"Number {number} doesnt appear in the array")


