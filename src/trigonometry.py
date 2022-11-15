
from .functions import fact

def sin_ts(angle: float, n: int):
    # Returns a sine of the given angle (in radians)
    # calculated by using a simplified version
    # of the Taylor series
    # (without the need for factorial functions)
    # https://en.wikipedia.org/wiki/Taylor_series#Trigonometric_functions

    if type(angle) not in [float, int]:
        raise TypeError("Invalid input provided. Angle must be a real number.")

    if type(n) is not int:
        raise TypeError("Invalid input provided. Int type argument expected.")

    tmp = angle
    sine = tmp

    for i in range(1, n):
        mult = (-angle * angle) / ((2 * i + 1) * (2 * i))
        tmp *= mult
        sine += tmp
    
    return round(sine, 10)


def cos_ts(angle: float, n: int):
    # Returns a cosine of the given angle (in radians)
    # calculated by using the Taylor series
    # https://en.wikipedia.org/wiki/Taylor_series#Trigonometric_functions

    if type(angle) not in [float, int]:
        raise TypeError("Invalid input provided. Angle must be a real number.")

    if type(n) is not int:
        raise TypeError("Invalid input provided. Int type argument expected.")

    cosine = 0.0

    for i in range(n):
        cosine += (((-1) ** i) / (fact(2 * i))) * (angle ** (2 * i))
    
    return round(cosine, 10)


def tg_ts(angle: float, n: int):
    pass

# TODO (wddkarz): Add a tg and ctg functions
