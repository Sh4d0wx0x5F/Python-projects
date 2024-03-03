class Node:

    def __init__(self, item):
        self.__left = None
        self.__right = None
        self.__item = item

    def insert(self, item):

        if self.__item:
            if item < self.__item:
                if self.__left is None:
                    self.__left = Node(item)
                else:
                    self.__left.insert(item)
            elif item > self.__item:
                if self.__right is None:
                    self.__right = Node(item)
                else:
                    self.__right.insert(item)

        else:
            self.__item = item

    def search(self, key):
        if key == self.__item:
            return True
        elif key < self.__item and self.__left is not None:
            return self.__left.search(key)
        elif key > self.__item and self.__right is not None:
            return self.__right.search(key)
        else:
            return False

node_1 = Node(15)
for i in range(6):
    node_1.insert(int(input("Enter value: ")))

print(node_1.search(int(input("Enter value to search: "))))
