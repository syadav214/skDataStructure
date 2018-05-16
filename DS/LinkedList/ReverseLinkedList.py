"""
Reverse the LinkedList
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
    
    def _print(self):
        node = self.currnode
        while node:
            print node.data
            node = node.next
       
    def ReverseList(self):
        prev_node = None
        currentHead = self.currnode       
    
        while currentHead:
            copy_prev_node = prev_node
            copy_next_node = currentHead.next

            prev_node = currentHead
            currentHead.next = copy_prev_node
            currentHead = copy_next_node
    
        self.currnode = prev_node
        return prev_node
       
if __name__ == "__main__":
    li = LinkedList()
    li.add(2)
    li.add(4)
    li.add(5)
    li.ReverseList()
    li._print()