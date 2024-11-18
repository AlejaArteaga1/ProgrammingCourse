## Exercise 2

"""
Please create a function that return a list of odd numbers of input list

Example

input = [2,2,3,4,4,6,7,8,9,10]

output

[2,2,4,4,6,8,10] """

list = [2,2,3,4,4,6,7,8,9,10]
def list_odd_numbers(list):
    odd_numbers= []
    for number in list:
        if number % 2 != 0:
            odd_numbers.append(number)
    return odd_numbers

print(list_odd_numbers(list))