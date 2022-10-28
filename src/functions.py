
from tkinter import Y


def sum_arr(array: list):
    # Returns a sum of the array elements

    if type(array) is not list:
        raise TypeError("Invalid input provided. List type argument expected.")

    sum = 0
    for element in array:
        if type(element) not in [int, float]:
            raise TypeError("Invalid input provided. Every array element must be a real number.")
        
        sum += element
    
    return sum


def product_arr(array: list):
    # Returns a multiplication of the array elements

    if type(array) is not list:
        raise TypeError("Invalid input provided. List type argument expected.")
    
    prod = array[0]
    for element in array:
        if type(element) not in [int, float]:
            raise TypeError("Invalid input provided. Every array element must be a real number.")
        
        prod *= element

    return prod


# TODO (wedkarz): implement a better algorithm
def fact(number: int):
    # Returns a factorial of the input integer

    if type(number) is not int:
        raise TypeError("Invalid input provided. Int type argument expected.")
    
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i

    return factorial


# TODO (wedakrz): add invalid input checking
def exponent(base: int, exp: int):
    # Returns a value of an integer base raised to an integer exponent
    # Using exponentation by squaring algorithm
    # https://en.wikipedia.org/wiki/Exponentiation_by_squaring

    if exp < 0:
        base = 1 / base
        exp *= -1
    
    if exp == 0:
        return 1
    
    tmp = 1
    while exp > 1:
        if exp & 1 == 0:
            base *= base
            exp = exp / 2
        else:
            tmp *= base
            base *= base
            exp = (exp - 1) / 2
    
    return base * tmp

