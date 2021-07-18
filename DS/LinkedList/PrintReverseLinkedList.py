"""
Print Linked List in reserve order.
We need to get to end of the linked list by calling recurvise function with parameter next node.
And then please data of each node.
"""

class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__ (self):
        self.currnode = None

    def add(self,data):
        newNode = Node(data,self.currnode)
        self.currnode = newNode
        return self.currnode
    
    def printR(self,head):
        print 'Start Fun'
        if head:
            print 'Before recurvise'
            self.printR(head.next)
            print 'After recurvise'
            print head.data
       
if __name__ == "__main__":
    li = LinkedList()
    li.add(2)
    li.add(4)
    node = li.add(5)
    li.printR(node)