
def linked_list_from_string(s):
    nodes_data = s.split(' -> ')
    nodes_data.pop() # remove the trailing None
    if not nodes_data:
        return None
    head = Node(int(nodes_data.pop()), next=None)
    while nodes_data:
        data = nodes_data.pop()
        new_node = Node(int(data), next=head)
        head = new_node
    return head