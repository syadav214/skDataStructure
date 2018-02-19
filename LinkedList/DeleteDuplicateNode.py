# Delete duplicate-value nodes from a sorted linked list

class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.currnode = None

    def add(self,data):
        newNode = Node(data,self.currnode)
        self.currnode = newNode
        return self.currnode
    
    def printList(self,head):
        while head:
            print head.data
            head = head.next
    
    def RemoveDuplicates(self,head):
        if head:
            node = head
            while head.next:
                if head.data == head.next.data:
                    head.next = head.next.next
                else:
                    head = head.next
        return node      
    
if __name__ == "__main__":
    li = LinkedList()
    li.add(1)
    li.add(1)
    head1 = li.add(2)
    li.printList(head1)
    print "__________"
    head2 = li.RemoveDuplicates(head1)
    li.printList(head2)