p_x = int(input("Enter x coordinate of P point: "))
p_y = int(input("Enter y coordinate of P point: "))

if p_x > 0 and p_y > 0:
    pos = "first"
elif p_x < 0 and p_y > 0:
    pos = "second"
elif p_x < 0 and p_y < 0:
    pos = "third"
elif p_x > 0 and p_y < 0:
    pos = "fourth"
else:
    pos = "on the line"

if pos == "first" or pos == "second" or pos == "third" or pos == "fourth":
    print(f"Point P({p_x},{p_y}) is in the {pos} quadrant of the coordinate system")
else:
    print(f"Point P({p_x},{p_y} is {pos}")