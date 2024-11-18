## Exercise 2
"""
Return the last vowel position in optimal form, 
in case the word dont have vowel the result must be -1. 

Use a for statement,
Why is not more optimal than use while? Explain """
vowels = ["a","e","i","o","u"]

def isVowel (letter):
    letter = letter.lower()
    for vowel in vowels:
        if letter == vowel:
            return True
    return False

def last_vowel_position(word):
    for i in range(len(word) -1, -1, -1):
        if isVowel(word[i]):
            return i
    else:
        return -1

print(last_vowel_position("Trace")) # Expect 4