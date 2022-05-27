class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
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
            self.tail.next = node_to_add
            self.tail = node_to_add
        self.length += 1
        return True

    def prepend(self, value):
        node_to_add = Node(value)
        if self.length == 0:
            self.head = node_to_add
            self.tail = node_to_add
        else:
            node_to_add.next = self.head
            self.head = node_to_add
        self.length += 1
        return True

    def insert(self, index, value):
        pass

    def pop(self):
        """Pop off a node at the end of the list"""
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value


my_linked_list = LinkedList(4)

print(my_linked_list.head.value)
my_linked_list.append(11)
print(my_linked_list.tail.value)

print(my_linked_list.print_list())
print(my_linked_list.pop())
print(my_linked_list.pop())
print(my_linked_list.pop())
