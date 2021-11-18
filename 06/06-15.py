array = ['blue', 'red', 'green', 'black']

textfile = open("06-15 list.txt", "w")

for i in array:
    textfile.write(i + "\n")
textfile.close()