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
"""

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
    





