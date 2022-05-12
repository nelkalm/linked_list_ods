# Implements class Node, storing data x and reference next.

class Node:

    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next
    
    def get_value(self):
        return self.value
    
    def set_value(self, new_value):
        self.value = new_value
    
    def get_next(self):
        return self.next
    
    def set_next(self, new_next):
        self.next = new_next
