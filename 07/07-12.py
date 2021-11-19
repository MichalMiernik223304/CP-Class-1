file = open("shopping.txt", "a")
name = input("Enter product: ")
file.write(name)
file.close()