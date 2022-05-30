class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
        new_node.next = self.top
        self.top = new_node
        self.height += 1

    def pop(self):
        if self.top is None:
            return None
        top_node = self.top
        self.top = self.top.next
        top_node.next = None
        self.height -= 1
        return top_node
    
    def peek(self):
        if self.top is None:
            return None
        return self.top.value


my_stack = Stack(4)
my_stack.push(1)
my_stack.push(2)
my_stack.print_stack()
print(my_stack.peek())
# my_stack.pop()
# my_stack.print_stack()
