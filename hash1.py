"""
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')

root.left=nodeA
root.right=nodeB


nodeA.left= nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

print("root.right.left.data:",root.right.left.data)



#a PREORDER TRAVASEL
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def preOederTraversal(node):
    if node is None:
        return
    print(node.data,end =",")
    preOederTraversal(node.left)
    preOederTraversal(node.right)

root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

preOederTraversal(root)


#Binary Search Tree (BTS)

class TreeNode:
    def __init_ (self,data):
        self.data = data
        self.left = None
        self.right = None

def inOrderTraversal(node):
    if node is None:
        return
    
    inOrderTraversal(node.left)
    print(node.data,end=",")

    inOrderTraversal(node.right)

root = TreeNode(13)
node7 = TreeNode(7)
node15 = TreeNode(15)
node3 = TreeNode(3)
node8 = TreeNode(8)
node14 = TreeNode(14)
node19 = TreeNode(19)
node18 = TreeNode(18)

root.left = node7
root.right = node15

node7.left = node3
node7.right = node8

node15.left = node14
node15.right = node19

node19.left = node18

inOrderTraversal(root)
 """


 #AVL trees
 # 

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

def getHeight(node):
    if not node:
        return 0
    return node.height

def getBalance(node):
    if not node:
        return 0
    return node.height

def getBalance(node):
    if not node:
        return 0
    return getHeight(node.left)- getHeight(node.right)

def rightRotate(y):
    print ('Rotate right on mode',y.data)
    x=y.left
    T2 = x.right
    x.right = y
    y.left = T2
    y.height = 1 + max(getHeight(y.left),getHeight(y.right))
    x.height = 1+ max(getHeight(x.left),getHeight(x.right))

    return x

def leftRotate(x):
    print('Rotate left on node',x.data)
    y=x.right
    T2=y.left
    y.left = x
    x.right = T2
    x.height = 1+max(getHeight(x.left),getHeight(x.right))
    y.height = 1+max(getHeight(y.left),getHeight(y.right))
    return y

def insert(node,data):
    if not node:
        return TreeNode(data)
    
    if data <  node.data:
        node.left = insert (node.left,data)
    elif data > node.data:
        node.right = insert (node.right,data)

  # Update the balance factor and balance the tree

    node.height = 1+max(getHeight(node.left),getHeight(node.right))
    balance = getBalance(node)
    # Balancing the tree
  # Left Left
    if balance > 1 and getBalance(node.left)<0:
        node.left = leftRotate(node.left)
        return rightRotate(node)
    
    if balance < -1 and getBalance(node.right) >0:
        node.right = rightRotate(node.right)
    return leftRotate(node)

def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data,end=",")
    inOrderTraversal(node.right)
    #Inserting nodes

root = None
letters = ['C','B','E','A','D','H','G','F']

for letter in letters:
    root = insert(root,letter)

inOrderTraversal(root)
    
    




   




