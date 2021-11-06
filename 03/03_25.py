a = 4
b = 15

for i in range(1, a+1):
    if i == 1:
        print(b * "*")
    elif i > 1 and i < a:
        print("*"+(b-2)*" "+"*")
    else:
        print(b * "*")
