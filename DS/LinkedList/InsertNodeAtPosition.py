#Insert Node At a specific Position

class Node:
    def __init__ (self,data,next):
        self.data= data
        self.next = nextnode

class LinkedList:
    def __init__ (self):
        self.currnode = None
    
    def addNode(self, data):
        node = Node(data,self.currnode)
        self.currnode = node
    
    def InsertNth(head,data,position):
        if head is None or position == 0:
            return Node(data,head)
        else:
            cur_pos = 1
            cur_node = head
            while cur_node.next and cur_pos < position:
                cur_node = cur_node.next
                cur_pos += 1
            cur_node.next = Node(data,cur_node.next)
        return head