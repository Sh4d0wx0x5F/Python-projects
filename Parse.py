def parse(INString):
    new_string = ""
    total = 0
    count = 0
    x = len(INString)
    for y in range(x):
        nxtchar = INString[y]
        if nxtchar != ",":
            new_string = new_string + nxtchar
        else:
            total = total + int(new_string)
            count = count + 1
            new_string = ""

    total = total + int(new_string)
    count = count + 1
    avg = total / count
    print(f" the total : {total}")
    print(f" the average : {avg}")


parse("12,13,451,22")
