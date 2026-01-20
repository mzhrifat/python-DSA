#Check if a value exists in a list:
"""
mylist= [3,7,2,9,5,1,8,4,6]

if 4 in mylist:
    print("Found!")
else:
    print("Not Found!")
"""

#2 Find the index of a value in a list:

def linearSearch(arr,targetVAl):
    for i in range (len(arr)):

        if arr[i]== targetVAl:
            return -1
mylist = [3,7,2,9,5,1,8,4,6]
x=4

result = linearSearch(mylist,x)

if result != -1:
    print("Found  at index",result)
 
else:
    print("Not found")

