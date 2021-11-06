n = int(input("Enter value:"))

prime_counter = 0
ins_counter = 0
number = 1
i = 1
prime_list = []

while prime_counter < n:
    for i in range(1, number+1):
        if number % i == 0:
            ins_counter = ins_counter + 1
    if ins_counter <= 2:
        prime_counter = prime_counter + 1
        prime_list.append(number)

    number = number + 1
    ins_counter = 0

for i in range(1, n+1):
    if n % i == 0:
        ins_counter = ins_counter + 1


if ins_counter <= 2:
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")

print(f"First {n} prime numbers: {prime_list}")