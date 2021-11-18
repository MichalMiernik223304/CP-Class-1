def compare(array1, array2):
    comp = False
    if len(array1) == len(array2):
        for i in range(len(array1)):
            if array1[i] == array2[i]:
                comp = True
            else:
                comp = False
                break
    else:
        comp = False

    print(f"Array1: {array1}")
    print(f"Array2: {array2}")

    if comp == False:
        print(f"Comparison: arrays are not the same")
    else:
        print(f"Comparison: arrays are the same")

array1 = ["water", "book", "sky"]
array2 = ["water", "book", "sky"]

compare(array1, array2)