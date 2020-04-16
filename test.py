class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def add(self, data):
        if(self.data):
            if(data < self.data):
                if(self.left == None):
                    self.left = Node(data)
                else:
                    self.left.add(data)
            elif(data > self.data):
                if(self.right == None):
                    self.right = Node(data)
                else:
                    self.right.add(data)
        else:
            self.data = data
    
    def inOrderPrintTree(self,root):
        if(root != None):
            self.inOrderPrintTree(root.left)
            print(root.data)
            self.inOrderPrintTree(root.right)

    def maxDepth(self, root):
        if(root == None):
            return 0
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        if(leftDepth> rightDepth):
            return leftDepth + 1
        else:
            return rightDepth + 1
    
    def verticalSum(self,root,hd,hm):
        if(root == None):
            return
        self.verticalSum(root.left, hd - 1, hm)
        print('hd',hd,'data',root.data)
        if(hd in hm):
            prevSum = hm[hd]
        else:
            prevSum = 0
        hm[hd] = prevSum + root.data
        self.verticalSum(root.right, hd + 1, hm)
        



root = Node(10)
root.add(8)
root.add(5)
root.add(9)
root.add(20)
root.add(15)
root.add(13)
#root.inOrderPrintTree(root)
#print('--------------')
#print(root.maxDepth(root))
hm = {}
root.verticalSum(root,0,hm)
print(hm[0])





