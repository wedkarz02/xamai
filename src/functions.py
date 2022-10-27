
def sum_arr(array: list):
    """ Returns a sum of the array elements """

    if type(array) is not list:
        raise TypeError("Invalid input provided. List type argument expected.")

    sum = 0
    for element in array:
        if type(element) not in [int, float]:
            raise TypeError("Invalid input provided. Every array element must be a real number.")
        
        sum += element
    
    return sum


def product_arr(array: list):
    """ Returns a multiplication of the array elements """

    if type(array) is not list:
        raise TypeError("Invalid input provided. List type argument expected.")
    
    prod = array[0]
    for element in array:
        if type(element) not in [int, float]:
            raise TypeError("Invalid input provided. Every array element must be a real number.")
        
        prod *= element

    return prod
