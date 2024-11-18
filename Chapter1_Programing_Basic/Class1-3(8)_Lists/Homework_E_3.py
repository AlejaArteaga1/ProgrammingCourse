## Exercise 3

"""
Please create a function that return a list of two lists with odd and even separate numbers of input list

Example

input = [2,2,3,4,4,6,7,8,9,10]

output

[ [2,2,4,4,6,8,10] , [3,7,9] ] """

list = [2,2,3,4,4,6,7,8,9,10]
def list_odd_and_even_numbers(list):
    odd_numbers = [] 
    even_numbers = []
    list2 = [ odd_numbers, even_numbers]
    for number in list:
        if number % 2 == 0:
            odd_numbers.append(number)
        else: 
            even_numbers.append(number)
    return list2
print(list_odd_and_even_numbers(list))
