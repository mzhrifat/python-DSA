#Traversal of a singly linked list in Python
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def traverseAndPrint(head):
    currenetNode = head
    while currenetNode:
        print(currenetNode.data,end = "->")
        currenetNode =currenetNode.next
    print ("null")

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

traverseAndPrint(node1)



#Finding the lowest value in a singly linked list in Python:

def findLowestValuse(head):
    minValue = head.data
    currentNode = head.next
    while currentNode:
        if currentNode.data < minValue:
            minvalue =currentNode.data
            currentNode = currentNode.next
        return minvalue
    
node1 = Node(7)
node2 =Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
print("The lowest value in the linked list is :".findLowestvaluse(node1))



#Deleting a specific node in a singly linked list in Python:

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def traverseAndPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data,end = "->")
        print("null")

def deleteSpecificNode(head,nodeToDelete):
    if head == nodeToDelete:
        return head.next
    
    currentNode = head
    while currentNode.next and currentNode.next != nodeToDelete:
     currentNode= currentNode.next

     if currentNode.next is None:
         return head
     
     currentNode.next = currentNode.next.next

     return head


node1= Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Before deletion:")
traverseAndPrint(node1)

#Delete node4
node1= deleteSpecificNode(node1,node4)

print("\nAfter deletion :")
traverseAndPrint(node1)

"""

#Inserting a node in a singly linked list in Python
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def traverseAndPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data,end="->")
        currentNode = currentNode.next
        print("null")

def insertNodeAtPosition(head,newNode,position):
    if position == 1:
        newNode.next = head
        return newNode
    
    currentNode = head
    for _ in range(position -2):
        if currentNode is None:
            break 
        currentNode =currentNode.next

    newNode.next = currentNode.next
    currentNode.next = newNode
    return head

node1 = Node(7)
node2 = Node(3)
node3 = Node(2)
node4 = Node(9)

node1.next = node2
node2.next = node3
node3.next  = node4

print("Orginal list:")
traverseAndPrint(node1)

# Insert a new node with value 97 at position 2

newNode = Node(97)
node1= insertNodeAtPosition(node1,newNode,2)

print("\nAfter insertion : ")
traverseAndPrint(node1)