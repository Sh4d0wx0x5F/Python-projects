class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None


class LinkedList:
    def __init__(self):
        self.__head = None

    def append(self, data):
        new_node = Node(data)
        if self.__head is None:
            self.__head = new_node
            return
        last_node = self.__head
        while last_node.__next:
            last_node = last_node.__next
        last_node.__next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.__next = self.__head
        self.__head = new_node

    def delete_node(self, key):
        current_node = self.__head
        if current_node and current_node.__data == key:
            self.__head = current_node.__next
            current_node = None
            return
        prev = None
        while current_node and current_node.__data != key:
            prev = current_node
            current_node = current_node.__next
        if current_node is None:
            return
        prev.__next = current_node.__next
        current_node = None

    def print_list(self):
        current_node = self.__head
        while current_node:
            print(current_node.__data)
            current_node = current_node.__next


# Example usage
if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.prepend(0)
    linked_list.print_list()
    print("After deletion:")
    linked_list.delete_node(2)
    linked_list.print_list()
