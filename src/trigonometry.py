
#TODO (wedkarz): Add documentation and result rounding
def sin_ts(angle: float, n: int):
    tmp = angle
    sine = tmp

    for i in range(1, n):
        mult = (-angle * angle) / ((2 * i + 1) * (2 * i))
        tmp *= mult
        sine += tmp
    
    return sine
