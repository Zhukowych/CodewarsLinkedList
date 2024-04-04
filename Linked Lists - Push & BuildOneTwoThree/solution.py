from preloaded import Node

'''
Node is defined in preloaded like this:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
    
def push(head, data):
    if not head:
        head = Node(data=data)
        return head
    
    new_node = Node(data)
    new_node.next = head
    return new_node
    
    
def build_one_two_three():
    head = None
    head = push(head, 3)
    head = push(head, 2)
    head = push(head, 1)
    return head
    