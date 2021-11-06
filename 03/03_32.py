num = 1
n = 49
list = []
rows = 7
start = 0
columns = 0

if n % rows == 0:
    columns = int(n / rows)
else:
    columns = int((n / rows) + 1)

for j in range(rows):
    start = start + 1
    num = start
    for i in range(columns):
        list.append(num)
        num = num + rows
        if num >= n+1:
            break
    print(list)
    list = []
