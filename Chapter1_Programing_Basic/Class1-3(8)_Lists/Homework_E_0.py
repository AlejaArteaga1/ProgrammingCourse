## Exercise 0
# Please create a function to create a list to 1 to max_number

""" 
Example
n = 10

Output

[1,2,3,4,5,6,7,8,9,10] """
n = 25
def create_counter_list(max_number):
    list =[]
    for i in range(1, max_number + 1):
        list.append(i)
    return list
print(create_counter_list(n))