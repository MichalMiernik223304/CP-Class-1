weight = int(input("Enter your weight in kg:"))
height = int(input("Enter your height in cm:"))
bmi = round(weight/(height/100)**2, 1)

print(f"BMI index: {bmi}")
