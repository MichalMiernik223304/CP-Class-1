array = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
longest = ""
for i in range(0, len(array)-1):
    if len(array[i]) > len(longest):
        longest = array[i]

print("Names:", end=" ")
print(*array)
print(f"Longest name: {longest}")