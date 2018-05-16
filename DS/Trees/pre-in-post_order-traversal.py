# Traverse binary Tree
# if print root.data, then it will print next after a space due to ','

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.currTree = None
    
    def addNode(self,data):
        if self.currTree == None:
            self.currTree =  Node(data)
        else:
            self._addNode(data,self.currTree)
        return self.currTree
    
    def _addNode(self,data,node):
        if data < node.data:
            if node.left != None:
                self._addNode(data,node.left)
            else:
                node.left = Node(data)
        else:
            if node.right != None:
                self._addNode(data,node.right)
            else:
                node.right = Node(data)   

    def PreOrderPrintNode(self,node):
        if node != None:
            print node.data
            self.PreOrderPrintNode(node.left)           
            self.PreOrderPrintNode(node.right)

    def InOrderPrintNode(self,node):
        if node != None:
            self.InOrderPrintNode(node.left)
            print node.data
            self.InOrderPrintNode(node.right)
    
    def PostOrderPrintNode(self,node):
        if node != None:
            self.PostOrderPrintNode(node.left)            
            self.PostOrderPrintNode(node.right)
            print node.data

if __name__ == "__main__":
    tr = Tree()
    tr.addNode(20)
    tr.addNode(3)
    node = tr.addNode(1)
    tr.InOrderPrintNode(node)
