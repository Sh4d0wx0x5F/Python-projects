def bsort(name):
    name.sort()

name = ["Joe", "Roger", "Beckham", "Alice"]

print("Name array before sort")
for x in range(4):
    print(name[x])

bsort(name)
print("Name array after sort")
for x in range(4):
    print(name[x])
