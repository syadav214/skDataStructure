# Find the node at the given position counting backwards from the tail

class Node:
    def __init__(self,data,next):
        self.data= data
        self.next = next

class LinkedList:
    def __init__(self):
        self.currnode = None
    
    def add(self,data):
        newNode = Node(data,self.currnode)
        self.currnode = newNode
        return self.currnode
    
    def printlist(self,head):
        while head:
            print head.data
            head = head.next
    
    def getVal(self,head,pos):
        tempnode = head
        currpos = 0
        while head:
            if currpos > pos:
                tempnode = tempnode.next
            head = head.next
            currpos += 1
        
        print tempnode.data
    
if __name__ == "__main__":
    li = LinkedList()
    li.add(2)
    li.add(1)
    node1 = li.add(3)
    li.printlist(node1)
    print "getVal"
    li.getVal(node1,2)