"""
Delete Node At a specific Position
If Position is 0 then return the nextnode. [So, setting next node to head Position means delete head node.]
else need to set nextnode in recursive with decrementing Position.
"""

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
    
    def Delete(head, position):        
        if position == 0:
            return head.next
        head.next = Delete(head.next, position - 1)
        return head