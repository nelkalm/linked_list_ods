from node import Node

class DoublyLinkedList:
    
    def __init__(self) -> None:
        self.length = 0
        dummy = Node(None)
        dummy.prev = dummy
        dummy.next = dummy

    def get_node(self, node_index):
        if node_index < self.length / 2:
            node = self.dummy.next
            for _ in range(node_index):
                node = node.next
        else:
            node = self.dummy.next
            for _ in range(self.length - node_index):
                node = node.prev
        return node

    def get_element(self, value):
        pass

    def set_node_value(self, node_index, value):
        pass

    def add_before(self, node_to_add, value):
        pass

    def add(self, node_index, value):
        pass

    def remove_node(self, node_to_remove):
        pass

    def remove(self, node_index):
        pass
