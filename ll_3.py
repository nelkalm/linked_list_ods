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

    def get(self, index):
        """Gets a node at a given index in the parameter."""
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False

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
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        else:
            node_to_insert = Node(value)
            # temp = self.head
            # pre = self.head
            # for _ in range(index):
            #     pre = temp
            #     temp = temp.next
            # pre.next = node_to_insert
            # node_to_insert.next = temp
            # self.length += 1

            temp = self.get(index - 1)
            node_to_insert.next = temp.next
            temp.next = node_to_insert
            self.length += 1
            return True

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

    def pop_first(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
            if self.length == 0:
                self.tail = None
            return temp.value
    
    def remove(self, index):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.pop_first()
        if index == self.length:
            return self.pop()
        else:
            target_node = self.get(index)
            node_before_target = self.get(index - 1)
            node_after_target = self.get(index + 1)
            node_before_target.next = node_after_target
            target_node.next = None
            self.length -= 1


my_linked_list = LinkedList(4)
my_linked_list.prepend(5)
my_linked_list.prepend(6)
my_linked_list.prepend(7)
print(my_linked_list.print_list())
my_linked_list.insert(2, 3)
print(my_linked_list.print_list())
my_linked_list.remove(2)
print(my_linked_list.print_list())
