#Create a Hash Function that sums the Unicode numbers of each character and return a number between 0 and 9:

def has_function(value):
    sum_of_chars = 0
    for char in value:
        sum_of_chars += ord(char)

    return sum_of_chars % 10
print(" 'Bob' has has code: ",has_function('Bob'))