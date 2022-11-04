list1 = [6, 3, 534, 4323, 32, 61]


y = -1
z = 0

for i in list1:
    y = -1
    z = 0

    while z < len(list1) - 1:
        if list1[y+1] > list1[z+1]:
            list1[y+1], list1[z+1] = list1[z+1], list1[y+1]
        y = y+1
        z = z+1

print(list1)
