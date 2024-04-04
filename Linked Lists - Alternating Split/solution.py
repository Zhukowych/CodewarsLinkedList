class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def push(head, tail, node):
    if not head:
        head = node
        tail = node
    else:
        tail.next = node
    node.next = None
    tail = node
    return head, tail
    
def alternating_split(head):
    if not head or not head.next:
        raise ValueError()

    first_head, first_tail = None, None
    second_head, second_tail = None, None
    
    current = head
    counter = 0
    while current:
        next = current.next
        if counter % 2 == 0:
            first_head, first_tail = push(first_head, first_tail, current)
        else:
            second_head, second_tail = push(second_head, second_tail, current)
        current = next
        counter += 1
    
    return Context(first_head, second_head)
