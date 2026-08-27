import math 

def is_number(number: str) -> bool:
    try:
        return math.isfinite(number)
    except ValueError, TypeError:
        return False


print(is_number("ee"))