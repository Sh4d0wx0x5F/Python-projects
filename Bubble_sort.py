def bsort(name):
    flag = False
    for i in range(len(name) - 1, 0, -1):
        for j in range(i):
            if name[j] > name[j + 1]:
                temp = name[j]
                name[j] = name[j + 1]
                name[j + 1] = temp
                flag = True
        if flag == False:
            break

name = ["Joe", "Roger", "Beckham", "Alice"]

print("Name array before sort")
for x in range(4):
    print(name[x])

bsort(name)
print("Name array after sort")
for x in range(4):
    print(name[x])
