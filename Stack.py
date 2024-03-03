stack = [None for index in range(0, 10)]
base_pointer = 0
top_pointer = -1
stack_full = 10
item = None


def pop():
    global top_pointer, base_pointer, item

    if top_pointer == base_pointer - 1:
        print("Stack is empty, cannot pop")
    else:
        item = stack[top_pointer]
        top_pointer -= 1


def push(item):
    global top_pointer

    if top_pointer < stack_full - 1:
        top_pointer += 1
        stack[top_pointer] = item
    else:
        print("Stack is full, cannot push")


for i in range(5):
    push(int(input("Enter an integer:\n")))

for x in range(2):
    pop()

print(stack)

print(top_pointer)
