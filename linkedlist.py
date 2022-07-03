class Node:


    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
    
    def get_value(self):
        return self.value
  
    def get_next_node(self):
        return self.next_node


class LinkedList:


    def __init__(self, value=None):
        self.head_node = Node(value)
  
    def get_head_node(self):
        return self.head_node
  
    def insert_beginning(self, new_value):
        print(f'\nInserting {new_value} into linked list')
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node