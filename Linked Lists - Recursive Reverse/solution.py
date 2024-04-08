
def reverse(head):

    def recursive(current, next):
        next_next = next.next
        next.next = current
        if not next_next:
            return next    
        return recursive(next, next_next)

    if not head or not head.next:
        return head
     
    reversed_head = recursive(head, head.next)
    head.next = None
    return reversed_head
