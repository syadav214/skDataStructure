#Find distance between two nodes of a Binary Tree
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.currTree = None
    
    def add(self,data):
        if(self.currTree == None):
            self.currTree = Node(data)
        else:
            self.addNode(data,self.currTree)
        
    def addNode(self,data,node):
        if(data < node.data):
            if(node.left != None):
                self.addNode(data, node.left)
            else:
                node.left = Node(data)
        else:
            if(node.right != None):
                self.addNode(data, node.right)
            else:
                node.right = Node(data)

    def PreOrderPrintNode(self,root):
        if root != None:
            print(root.data)
            self.PreOrderPrintNode(root.left)           
            self.PreOrderPrintNode(root.right)

    def pathToNode(self, root,path,k):
        if(root is None):
            return False
        
        path.append(root.data)

        if(root.data == k):
            return True
        
        if((root.left != None and self.pathToNode(root.left,path, k)) or (root.right != None and self.pathToNode(root.right,path, k))):
            return True
        
        path.pop()
        return False
    
    def distance(self,root, x,y):
        if root:
            path1 = []
            self.pathToNode(root,path1,x)
            print(path1)

            path2 = []
            self.pathToNode(root,path2,y)
            print(path2)

            i = 0
            while i < len(path1) and i < len(path2):
                if(path1[i] != path2[i]):
                    break
                i +=1
            
            return len(path1) + len(path2) - (2*i)
        else:
            return 0
    


t = Tree()
t.add(1)
t.add(2)
t.add(3)
t.add(4)
t.add(5)
t.add(6)
t.add(7)
t.add(8)
#t.PreOrderPrintNode(t.currTree)
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.right.right= Node(7) 
root.right.left = Node(6) 
root.left.right = Node(5) 
root.right.left.right = Node(8) 

print(t.distance(root,4,5))
