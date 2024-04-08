
def loop_size(node):
    slow = node
    fast = node
    while True:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            slow = slow.next
            fast = fast.next.next

            i = 0
            while slow != fast:
                slow = slow.next
                fast = fast.next.next
                i+=1
            return i + 1
