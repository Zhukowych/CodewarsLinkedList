

def sorted_insert(head, data):

    if not head:
        return Node(data)
    
    if data <= head.data:
        new_head = Node(data)
        new_head.next = head
        return new_head
    
    current = head
    while current.next:
        if current.data <= data <= current.next.data:
            tmp = current.next
            current.next = Node(data)
            current.next.next = tmp
            return head
        current = current.next
    
    current.head = Node(data)
    return head