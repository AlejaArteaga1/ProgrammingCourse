import fileinput


"""
Fix the code 

We know that the ingredients of Hamburger are:

meat, chicken, cheese, lettuce, tomatoes, onion, pickle

if we have >=1 vegetables the price increase 1  (expect pickles) 

if we have meat increase 2 , or if we have chicke increase 2
but if we have both increase only 3

Pickles increase 1 

All hamburgers have cheese and bread and the price is included 
Add more cases in main fn
"""

def price_hamburger(meat, chicken, cheese, lettuce, tomatoes, onion, pickle):
    price = 0
    if tomatoes or lettuce or onion:
        price += 1
    if pickle:
        price += 1
    if meat and chicken:
        price +=3
    elif meat or chicken:
        price +=2

    return price

print(price_hamburger(True, True, True, False, False, True, False))
