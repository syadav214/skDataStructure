#Print elements of linked list


class Node:
    def __init__ (self,data,nextnode):
        self.data= data
        self.nextnode = nextnode

class LinkedList:
    def __init__ (self):
        self.currnode = None
    
    def addNode(self, data):
        node = Node(data,self.currnode)
        self.currnode = node
    
    def _print(self):
        node = self.currnode
        while node:
            print node.data
            node = node.nextnode

lk = LinkedList()
lk.addNode(3)
lk.addNode(4)
lk.addNode(5)
lk._print()
