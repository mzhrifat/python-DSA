#Create a Hash Function that sums the Unicode numbers of each character and return a number between 0 and 9:
"""
def has_function(value):
    sum_of_chars = 0
    for char in value:
        sum_of_chars += ord(char)

    return sum_of_chars % 10
print(" 'Bob' has has code: ",has_function('Bob'))
"""

#According to our hash function, "Bob" should be stored at index 5.
#Lets create a function that add items to our hash table:
my_list = [None, None, None, None, None, None, None, None, None, None]

def has_function(value):
    sum_of_chars = 0
    for char in value:
        sum_of_chars +=ord(char)

    return sum_of_chars % 10

def add(name):
    index= has_function(name)
    my_list[index] = name

add ('Bob')
add('pete')
add('oggy')
add('siri')
add('ani')
print(my_list)