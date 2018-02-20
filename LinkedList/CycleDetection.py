#To check if a node is visited

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
    
    def has_cycle(self,head):
        if head is None:
            return False
        
        visited = []
        flag = 0
        node = head
        while node:
            if node not in visited:
                visited.append(node)
            else :
                flag = 1
                return True
            node = node.next
        
        if flag == 0:
            return False
                
    

if __name__ == "__main__":
    li = LinkedList()
    li.add(2)
    li.add(3)
    head = li.add(4)
    li.printList(head)
    print li.has_cycle(head)