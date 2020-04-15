class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def print(self):
        val = self.headval
        while val is not None:
            print(val.dataval)
            val = val.nextval

    def AtBegining(self,newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode

list1 = SLinkedList()
for i in range(10):
    e = Node(i)
    if(i==0):
        list1.headval = e
        prevNode = list1.headval 
    else:
        prevNode.nextval = e
        prevNode = e
list1.print()

