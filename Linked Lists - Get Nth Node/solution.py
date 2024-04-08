

def get_nth(node, index):
    i = 0
    if not node:
        raise ValueError()

    while i != index:
        if node.next:
            node = node.next
        else:
            raise IndexError()
        i+=1
    return node