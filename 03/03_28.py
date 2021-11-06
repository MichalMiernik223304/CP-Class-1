fib = 0
n1 = 0
n2 = 0

for i in range(1, 51):

    if i == 1:
        fib = 0
        n1 = 1
        print(fib, end=" ")
    else:
        n2 = n1
        n1 = fib
        fib = n1 + n2
        print(fib, end=" ")
