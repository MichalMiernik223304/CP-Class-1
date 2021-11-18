def rand_elem(array):
    import random
    return array[random.randint(0, len(array)-1)]

array = [55, 43, 23, 23, 1, 64, 42]

for i in range(5):
    print(rand_elem(array), end=" ")
