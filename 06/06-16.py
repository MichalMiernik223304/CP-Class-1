def stars(n):
    for i in range(0, len(n)):
        print(f"{n[i]}:", end=" ")
        print(n[i]*"*")


array = [12, 6, 4, 9, 3]
stars(array)