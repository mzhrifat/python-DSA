stack =[]
#push
stack.append('A')
stack.append('B')
stack.append('C')
print("stack:",stack)

#peek
topElement = stack[-1]
print("Peek:",topElement)

#pop
poppedElement = stack.pop()
print("Pop:",poppedElement)

#stack after pop
print("Stack after pop:",stack)

#isEmpty
isEmpty = not bool(stack)
print("isEmpty:",isEmpty)

#size
print("Size:",len(stack))
