height_cm = 170
height_fullfeet = int(int(height_cm/2.54) / 12)
height_inches = round(((height_cm/2.54 / 12) - height_fullfeet) * 12)

print(f"I am {height_cm}cm tall, i.e. {height_fullfeet} feet and {height_inches} inches.")