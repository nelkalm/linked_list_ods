from node import Node

class LinkedList:

    def __init__(self) -> None:
        self.length = 0
        self.head = None
        self.tail = None
    
    def push(self, value):
        new_node = Node(value)
        new_node.set_next = self.head
        self.head = new_node
        if self.length == 0:
            self.tail = new_node
        self.length += 1
        return value

    def pop(self):
        if self.length == 0:
            return None
        removed_node = self.head.get_value()
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return removed_node

    def remove(self):
        return self.pop()

    def add(self, value):
        added_node = Node(value)
        if self.length == 0:
            self.head = added_node
        else:
            self.tail = added_node
        self.tail = added_node
        self.length += 1
        return True

