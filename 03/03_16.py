num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))


if num_1 < num_2:
    asc_1 = num_1
    asc_2 = num_2
else:
    asc_1 = num_2
    asc_2 = num_1

print("Numbers in ascending order:", asc_1, asc_2)