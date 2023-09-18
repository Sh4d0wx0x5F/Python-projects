import os
import time

def clear():
    time.sleep(3)
    os.system('cls')

def create():
    file = open("myfile.txt", "w")
    for x in range(3):
        roll = input("Enter roll number: ")
        name = input(str("Enter name: "))
        marks = input("Enter marks: ")

        file.write(roll + "~" + name + "~" + marks + "\n")
    file.close()
    print("File has been created")

def append():
    file = open("myfile.txt", "a")
    for y in range(3):
        roll = input(str("Enter roll number: "))
        name = input(str("Enter name: "))
        marks = input(str("Enter marks: "))
        file.write(roll + "~" + name + "~" + marks + "\n")
    file.close()
    print("File has been appended")

def display():
    import io
    file_exists = os.path.exists('myfile.txt')
    if file_exists:
        file = io.open("myfile.txt", "r")
        line = file.read()
        while line != '':
            print(line)
            line = file.read()

        file.close()
    else:
        print("No file found")

def edit():
    file_r = open("myfile.txt", "r")
    file_w = open("temp.txt", "w")

    roll = str(input("Enter the roll number you want to edit: "))

    s = ' '
    while (s):
        s = file_r.readline()
        L = s.split("~")
        if len(s) > 0:
            if (L[0]) == roll:
                roll = input("Enter roll number: ")
                name = input("Enter name: ")
                mark = input("Enter marks: ")
                file_w.write(roll + "~" + name + "~" + mark + "\n")
            else:
                file_w.write(s)
    file_w.close()
    file_r.close()
    os.remove("myfile.txt")
    os.rename("temp.txt", "myfile.txt")
    print("Roll number has been edited")

def delete():
    file_r = open("myfile.txt", "r")
    file_w = open("temp.txt", "w")
    roll = str(input("Enter the roll number you want to delete: "))
    s = ' '
    while (s):
        s = file_r.readline()
        L = s.split("~")
        if len(s) > 0:
            if (L[0]) != roll:
                file_w.write(s)
    file_w.close()
    file_r.close()
    os.remove("myfile.txt")
    os.rename("temp.txt", "myfile.txt")
    print("Roll number has been deleted")

choice = 0
while choice != 6:
    clear()
    print(" 1 to create new a file Or Overwrite the existing one ")
    print(" 2 to append an existing file ")
    print(" 3 to Display a file ")
    print(" 4 to edit a file ")
    print(" 5 to delete a record ")
    print(" 6 to exit ")
    a = input(" Enter Your Choice ")

    if a == "1":
        create()
        choice = choice + 1
    elif a == "2":
        append()
        choice = choice + 1
    elif a == "3":
        display()
        choice = choice + 1
    elif a == "4":
        edit()
        choice = choice + 1
    elif a == "5":
        delete()
        choice = choice + 1
    elif a == "6":
        delete()
        choice = 6
    else:
        print(" wrong number press, enter again : ")
        a = input(" Enter Your Choice ")
