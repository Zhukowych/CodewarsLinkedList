def stringify(node):
    values = [] 
    while node:
        values.append(node.data)
        node = node.next
    values.append(None)
    return ' -> '.join(map(str, values))