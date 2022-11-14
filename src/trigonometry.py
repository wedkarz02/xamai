
from .functions import fact

# TODO (wedkarz): Add type checking
def sin_ts(angle: float, n: int):
    # Returns a sine of the given angle (in radians)
    # calculated by using a simplified version
    # of the Taylor series
    # (without the need for factorial functions)
    # https://en.wikipedia.org/wiki/Taylor_series#Trigonometric_functions

    tmp = angle
    sine = tmp

    for i in range(1, n):
        mult = (-angle * angle) / ((2 * i + 1) * (2 * i))
        tmp *= mult
        sine += tmp
    
    return sine


# TODO (wedkarz): Add documentation and type checking
def cos_ts(angle: float, n: int):
    cosine = 0.0

    for i in range(n):
        cosine += (((-1) ** i) / (fact(2 * i))) * (angle ** (2 * i))
    
    return cosine

