## Exercise 3

"""
Change list of digits (0 to 9) to list of letters

Hint: The list of the words is ORDERED.  """

words = ["zero","one","two","three","four","five","six","seven","eight","nine"]
listOfDigits = [2,5,1,9]
def change_to_words(listOfDigits):
    ans = []
    for digit in listOfDigits:
        ans.append(words[digit])
    return ans

print(change_to_words(listOfDigits)) # ["two","five","one","nine"]
