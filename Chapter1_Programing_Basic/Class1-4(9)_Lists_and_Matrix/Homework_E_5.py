## Exercise 6
"""
Create a list with the sum of the elements 
of each row.

Example 
| 1 | 0 | 1 |
| 4 | 1 | 0 |
| 0 | 5 | 1 |

Result :

[2,5,6]

    This method return the sum of the elemnts of rows. Your CAN'T 
    use "build-in" method sum() please implement with for statement
"""

matrix = [
    [1, 0, 1],
    [4, 1, 0],
    [0, 5, 1]
]

def calculate_sum_of_row(row):
    total = 0
    for number in row:
        total += number
    return total

def compute_sum_of_rows(matrix):
    ans = []
    for row in matrix:
        sum = calculate_sum_of_row(row)
        ans.append(sum)
    return ans

print(compute_sum_of_rows(matrix))
