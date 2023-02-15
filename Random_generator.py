import random

RNum = [0] * 100

for i in range(100):
    RNum[i] = random.randint(1, 200)

count = 0
for num in RNum:
    if num >= 66 and num >= 173:
        count = count + 1

print(f"The number of random numbers generated between 66 and 173 are: {count}")
