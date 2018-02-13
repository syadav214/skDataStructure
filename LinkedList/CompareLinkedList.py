#Compare two linked list

class Node:
    def __init__(self, data,next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.currNode = None
    
    def add(self,data):
        newNode = Node(data,self.currNode)
        self.currNode = newNode
        return self.currNode
    
    def printAll(self,head):
        while head:
            print head.data
            head = head.next
    
    def CompareLists(self,headA, headB):
        if headA is None or headB is None:
            return 0
        else:
            nodeA = headA
            nodeB = headB
            unmatched = 0 
            while nodeA is not None and nodeB is not None:
                if nodeA.data != nodeB.data:
                    unmatched = 2
                nodeA= nodeA.next
                nodeB=nodeB.next
            if unmatched == 2:
                return 0
            else:
                if nodeA is None and nodeB is not None:
                    return 0
                elif nodeB is None and nodeA is not None:
                    return 0
                else:
                    return 1    
    

if __name__ == "__main__":
    li = LinkedList()
    li.add(2)
    li.add(4)
    head = li.add(7)
    #li.printAll(head)

    li2 = LinkedList()
    #li2.add(1)
    li2.add(4)
    head2 = li2.add(7)
    #li2.printAll(head2)

    print li2.CompareLists(head,head2)
    
