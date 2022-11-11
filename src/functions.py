
def sum_range(array: list, start: int, end: int):
    # Returns a sum of the array elements in the range of <start, end>

    if type(array) is not list:
        raise TypeError("Invalid input provided. List type argument expected.")
    
    if type(start) is not int or type(end) is not int:
        raise TypeError("Invalid input provided. Int type arguments expected.")

    sum = 0
    for i in range(start, end):
        if type(array[i]) not in [int, float]:
            raise TypeError("Invalid input provided. Every array element must be a real number.")
        
        sum += array[i]
    
    return sum


def product_range(array: list, start: int, end: int):
    # Returns a multiplication of the array elements

    if type(array) is not list:
        raise TypeError("Invalid input provided. List type argument expected.")
    
    if type(start) is not int or type(end) is not int:
        raise TypeError("Invalid input provided. Int type arguments expected.")

    prod = array[start]
    for i in range(start, end):
        if type(array[i]) not in [int, float]:
            raise TypeError("Invalid input provided. Every array element must be a real number.")
        
        prod *= array[i]

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


def exponent(base: int, exp: int):
    # Returns a value of an integer base raised to an integer exponent
    # Using exponentation by squaring algorithm
    # https://en.wikipedia.org/wiki/Exponentiation_by_squaring

    if type(base) is not int or type(exp) is not int:
        raise TypeError("Invalid input provided. Int type arguments expected.")

    if exp < 0:
        base = 1 / base
        exp *= -1
    
    if exp == 0:
        return 1
    
    tmp = 1
    while exp > 1:
        if exp & 1 == 0:
            base *= base
            exp = exp // 2
        else:
            tmp *= base
            base *= base
            exp = (exp - 1) // 2
    
    return base * tmp


def normalize(value: float, min: float, max: float):
    # Returns a value rescaled to the range of <0, 1>
    # Using rescaling (min-max normalization)
    # https://en.wikipedia.org/wiki/Feature_scaling

    types = [int, float]
    if type(value) not in types or type(min) not in types or type(max) not in types:
        raise TypeError("Invalid input provided. Int or float type argument expected.")

    return (value - min) / (max - min)


def swap(array: list, a: int, b: int):
    # Swaps the array values at the index a and b

    if type(array) is not list:
        raise TypeError("Invalid input provided. List type argument expected.")
    
    if type(a) is not int or type(b) is not int:
        raise TypeError("Invalid input provided. Int type arguments expected.")

    array[a], array[b] = array[b], array[a]
