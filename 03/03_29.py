list = []
quantity = -1
num = 1

while num != 0:
    list.append(num)
    quantity = quantity + 1
    num = int(input("Enter number: "))

list.pop(0)
sum_list = sum(list)
mean = sum_list / quantity

print(f"RESULT: Quantity={quantity}, Sum={sum_list}, Mean={mean}")