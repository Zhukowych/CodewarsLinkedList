def remove_duplicates(head):
    
    if not head:
        return None
    
    if not head.next:
        return head
    
    previous = head
    current = head.next
    seen = {head.data}
    while current:
        if current.data in seen:
            previous.next = current.next
            current = current.next
        else:
            seen.add(current.data)
            tmp = current
            current = tmp.next
            previous = tmp
    
    return head


