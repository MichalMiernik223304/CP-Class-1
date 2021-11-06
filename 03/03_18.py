amount = int(input("Enter the amount in PLN: "))

coins_number_5 = 0
coins_number_2 = 0
coins_number_1 = 0

print(f"The amount of PLN {amount} in coins: ")

if amount > 0 and amount // 5 != 0:
    coins_number_5 = amount // 5
    amount = amount - coins_number_5 * 5

if amount > 0 and amount // 2 != 0:
    coins_number_2 = amount // 2
    amount = amount - coins_number_2 * 2

if amount > 0 and amount // 1 != 0:
    coins_number_1 = amount // 1
    amount = amount - coins_number_1 * 1

print(f"5 zł - {coins_number_5}")
print(f"2 zł - {coins_number_2}")
print(f"1 zł - {coins_number_1}")
