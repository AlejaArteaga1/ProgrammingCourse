## Exercise 4
"""
Please create a function that return a list of three lists with small , medium , and bigger words of a list of strings (words)
(The result lists can be empty)

Small (inclusive) : from 1 to 3 symbols
Medium (inclusive): from 4 to 7 symbols
Bigger (inclusive): 8 or more symbols

Example 0 

input = ["carretera", "sun", "casa","book", "compiler","now"]

output

[ ["sun","now"] , ["casa","book"], ["carretera","compiler"]]

Example 1

input = ["book","casa"]

output

[ [] , ["book","casa"], []] """

list = ["carretera", "sun", "casa","book", "compiler","now"]
def group_words_by_size(list):
    small = []
    medium = []
    bigger = []
    for word in list:
        if len(word) >= 1 and len(word) <= 3:
            small.append(word)
        elif len(word) >= 4 and len(word) <= 7:
            medium.append(word)
        elif len(word) >= 8:
            bigger.append(word)
    return [small, medium, bigger]

print(group_words_by_size(list))