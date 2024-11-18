## Exercise 4
"""
Find the max number of not empty matrix 
of positive numbers.
Print the position and the value.
In case that the maximum is repeated
can you print the first or the last"""
matrix = [[5,2,3],[19,23],[0,4,1,4]]

def find_maximum_matrix(matrix):
    max_number = matrix [0][0]
    max_position = (0, 0)
    for row in range(len(matrix)):
            for column in range(len(matrix[row])):
                if matrix[row][column] > max_number:
                    max_number = matrix[row][column] 
                    max_position = (row, column)
    return "Position: ", max_position, "Value:", max_number 

# Please test this scenary
print(find_maximum_matrix(matrix))
# Position 1, 1 Value 23
