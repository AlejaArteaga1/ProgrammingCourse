## Exercise 1

"""
Please create a function to count the odd numbers of a list

Example

input = [2,2,3,4,4,6,7,8,9,10]

output

7 
"""
list= [2,2,3,4,4,6,7,8,9,10]
def count_odd_numbers(list):
    position = 0
    for number in list:
        if number % 2 != 0:
            position +=1
    return position

print(count_odd_numbers(list))
