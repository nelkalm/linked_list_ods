class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next

    def enqueue(self, data):
        new_node = Node(data)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        self.last.next = new_node
        self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        removed_node = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        self.first = self.first.next
        removed_node.next = None
        self.length -= 1
        return removed_node


my_queue = Queue(4)
my_queue.enqueue(5)
my_queue.enqueue(15)
my_queue.print_queue()
print('-----')
my_queue.dequeue()
my_queue.print_queue()
