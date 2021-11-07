import mymath

x = False
y = mymath.generate_number()

while x == False:
    if mymath.read_number() == y:
        x = True
        print("OK")