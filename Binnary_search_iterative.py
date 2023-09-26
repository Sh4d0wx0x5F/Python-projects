def Binary_Search(arr, goal):
    upper_bound = len(arr) -1
    lower_bound = 0

    while upper_bound >= lower_bound:
        mid = (upper_bound + lower_bound) // 2

        if arr[mid] == goal:
            return mid

        elif goal < arr[mid]:
            upper_bound = mid - 1
        else:
            lower_bound = mid + 1
    return -1

name = ["a", "b", "c", "d", "e", "f"]
user = input(str("What name you are searching for ? \n"))
result = Binary_Search(name, user)

if result != -1:
    print(f"Element '{user}' found at index {result}")
else:
    print(f"Element '{user}' not found in the list")
