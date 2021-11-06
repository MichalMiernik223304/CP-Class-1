import math

a = int(input("Enter first side length:"))
b = int(input("Enter second side length:"))
c = int(input("Enter third side length:"))

p = (a + b + c)/2
s = round(math.sqrt(p*(p-a)*(p-b)*(p-c)), 2)

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
print(f"s = {s}")