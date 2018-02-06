#insert-a-node-at-the-tail-of-a-linked-list and return head


class Node:
    def __init__ (self,data,nextnode):
        self.data= data
        self.nextnode = nextnode

def Insert(head, data):
    if head == None:
        return Node(data, None)
    curr_node = head
    while curr_node.next != None:
        curr_node = curr_node.next
    curr_node.next = Node(data, None)
    return head
