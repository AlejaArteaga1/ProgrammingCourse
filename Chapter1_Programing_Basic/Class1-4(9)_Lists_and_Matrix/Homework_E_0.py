

## Exercise 0 
"""
Print a list in reverse without breaklines, 
you can *NOT* use .reverse() function"""

list = [1,2,3]
def print_reverse(list):
    for i in range(len(list), 0, -1): 
        print(i, end=" ") 

print_reverse(list) # Expect 3 2 1