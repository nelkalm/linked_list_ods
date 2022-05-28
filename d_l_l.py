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

    def pop_first(self):
        if self.length == 0:
            return False
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        else:
            new_node = Node(value)
            prev_node = self.get(index - 1)
            next_node = prev_node.next
            prev_node.next = new_node
            new_node.prev = prev_node
            new_node.next = next_node
            next_node.prev = new_node
            self.length += 1
            return True


my_doubly_linked_list = DoublyLinkedList(None)
my_doubly_linked_list.print_list()
my_doubly_linked_list.prepend(1)
my_doubly_linked_list.prepend(2)
my_doubly_linked_list.prepend(3)
my_doubly_linked_list.prepend(4)
my_doubly_linked_list.print_list()
my_doubly_linked_list.pop_first()
my_doubly_linked_list.print_list()
my_doubly_linked_list.set_value(1, 4)
my_doubly_linked_list.print_list()
my_doubly_linked_list.insert(1, 'a')
my_doubly_linked_list.print_list()
