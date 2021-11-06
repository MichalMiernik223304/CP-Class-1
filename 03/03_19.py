dog_years = int(input("Enter the dog's age in dog's years: "))
human_years = 0

if dog_years < 0 or dog_years > 40:
    print("Wrong value")

elif dog_years <= 2:
    human_years = dog_years * 10.5
    print(f"The dog's age in dog’s years is {human_years} years.")

elif dog_years > 2:
    human_years = (dog_years - 2) * 4 + 2 * 10.5
    print(f"The dog's age in dog’s years is {human_years} years.")