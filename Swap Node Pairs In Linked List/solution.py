from preloaded import Node

def swap_pairs(head):
    if not head:
        return None
    
    if not head.next:
        return head
    
    first = head
    end = None
    head = first.next
    while first and first.next:
        second = first.next
        second_next = second.next
        
        second.next = first
        first.next = second_next
        
        if end:
            end.next = second

        end = first
        first = second_next
            
    return head
