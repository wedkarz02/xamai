
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
