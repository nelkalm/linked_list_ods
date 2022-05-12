from node import Node

class LinkedList:

    def __init__(self) -> None:
        self.length = 0
        self.head = None
        self.tail = None
    
    def __str__(self):

        # defining a blank result variable
        result = ''

        # initializing pointer to head
        node = self.head

        # traversing SLL and adding to head
        while node:
            result += str(node.value) + ', '
            node = node.next
        
        # removing trailing commas
        result = result.strip(', ')

        # checking if anything is present in result
        if len(result):
            return '[' + result + ']'
        else:
            return '[]'
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
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
            self.tail.next = added_node
        self.tail = added_node
        self.length += 1
        return True


if __name__ == '__main__':
    my_sll = LinkedList()
    print(my_sll)

    my_sll.add('a')
    my_sll.add('b')
    my_sll.add('c')
    my_sll.add('d')
    my_sll.add('e')
    my_sll.add('x')
    print(my_sll)

    my_sll.remove()
    print(my_sll)

    my_sll.pop()
    print(my_sll)

    my_sll.push('y')
    print(my_sll)
