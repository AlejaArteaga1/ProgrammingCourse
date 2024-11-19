import fileinput
import Homework  

# Homework 1-1

"""
Complete the cases

https://www.geeksforgeeks.org/packing-and-unpacking-arguments-in-python/

What is unpack a variable?
Usamos unpack cuando tenemos los argumentos que queremos poner en otra variable, es decir, tenemos los argumentos que necesitamos en una sola variable y esa variable, al ser una sola, necesita ser puesta con (*variable) en la función que estamos haciendo. Desempaquetar la lista y pasar los elementos de esa lista como elementos individuales.
Why is it useful?
Es útil porque nos permite ahorrar código y almacenar una información del mismo tipo en una variable, y llamarla cuando sea necesario, en vez de dar nuevamente todos los parámetros que ya de por sí están asignados en una variable.
"""

def main():
    double = [True, True, True, True, True, True, True]
    single = [True, True, True, True, True, True, True]
    no_spicy = [True, False, True, True, True, True, False]  
    no_vegetables = [True, True, True, False, False, False, False]  

    single_price = Homework.price_hamburger(*single)
    double_price = Homework.price_hamburger(*double)
    nospicy_price = Homework.price_hamburger(*no_spicy)
    novegetables_price = Homework.price_hamburger(*no_vegetables)

    print("Single price:", single_price)
    print("Double price:", double_price)
    print("No spicy price:", nospicy_price)
    print("No vegetables price:", novegetables_price)


main()


