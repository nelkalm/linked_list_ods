class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        node_to_add = Node(value)
        if self.head is None:
            self.head = node_to_add
            self.tail = node_to_add
        else:
            node_to_add.prev = self.tail
            self.tail.next = node_to_add
            self.tail = node_to_add
        self.length += 1
        return True

    def prepend(self, value):
        node_to_add = Node(value)
        if self.head is None:
            self.head = node_to_add
            self.tail = node_to_add
        else:
            node_to_add.next = self.head
            self.head.prev = node_to_add
            self.head = node_to_add
        self.length += 1
        return True

    def pop(self):
        if self.head == 0:
            return False
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp


my_doubly_linked_list = DoublyLinkedList(7)
my_doubly_linked_list.print_list()
