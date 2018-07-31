#Merge two linked list in sorted order

class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.currNode = None
    
    def add(self,data):
        newNode = Node(data,self.currNode)
        self.currNode = newNode
        return newNode
    
    def printall(self,head):
        while head:
            print head.data
            head = head.next
    
    def merge(self,head1,head2):
        if head1 is None and head2 is None:
            return None
        elif head1 is None:
            return head2
        elif head2 is None:
            return head1
        
        if head1.data > head2.data:
            head2.next = self.merge(head1,head2.next)
            return head2
        else :
            head1.next = self.merge(head1.next, head2)
            return head1         

if __name__ == "__main__":
    li = LinkedList()
    li.add(2)
    head1 = li.add(3)
    #li.printall(head1)

    #print '----------'

    li2 = LinkedList()
    li2.add(4)
    head2 = li2.add(1)
    #li2.printall(head2)

    #print '----------'

    mergeList = li2.merge(head1,head2)
    li.printall(mergeList)
