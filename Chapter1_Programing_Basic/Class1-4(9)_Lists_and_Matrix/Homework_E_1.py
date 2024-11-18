## Exercise 1
"""
Return the first vowel position in optimal form,
in case the word dont have vowel the result must be -1"""


vowels = ["a","e","i","o","u"]

def isVowel (letter):
    letter = letter.lower()
    for vowel in vowels:
        if letter == vowel:
            return True
    return False

def first_vowel_position(word):
    i = 0
    for letter in word:
        if isVowel(letter):
            return i
        i += 1
    else:
        return -1


print(first_vowel_position("Trace")) # Expect 2
print(first_vowel_position("txt")) # Expect -1




