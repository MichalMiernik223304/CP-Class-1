temp_celsius = int(input('Enter temperature:'))  #typechange(read the temperature from the keyboard)
temp_kelvin = temp_celsius + 273.15  #define kelvin temperature using celsius degrees and formula
temp_fahrenheit = 32 +(9/5)*temp_celsius  #define fahrenheit temperature using celsius degrees and formula

print(f"Temperature in Celsius degrees: {temp_celsius}")
print(f"Temperature in Kelvins: {temp_kelvin}")
print(f"Temperature in Fahrenheit degrees: {temp_fahrenheit}")