
# TODO (wedkarz): add element type checking
def sum_arr(array: list):
    """ Returns a sum of the array elements """
    if type(array) is not list:
        raise TypeError("Invalid input provided. List type argument expected.")

    sum = 0
    for element in array:
        sum += element
    
    return sum


# TODO (wedkarz): add element type checking
def product_arr(array: list):
    """ Returns a multiplication of the array elements """
    if type(array) is not list:
        raise TypeError("Invalid input provided. List type argument expected.")
    
    prod = array[0]
    for element in array:
        prod *= element

    return prod
    
