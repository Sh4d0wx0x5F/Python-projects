name = ["Roger","Dean","Amber","Julie","Abraham","Watson","Emma"]

def linearSearch():
    found = False
    x = 0
    name_finder = input(str("What name you are searching for ? \n"))
    while x <= 6 and found == False:
        name_located = name[x]
        if name_finder == name_located:
            found = True
        x = x + 1
        if found == True:
            print(f'{name_finder} and your location is {x -1} ')
            break

linearSearch()
