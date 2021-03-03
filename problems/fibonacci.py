import math

def fibonacci(n):
    """
    Gives the nth Fibonacci number with accuracy up to the 70th value using Binet's Formula. 
    Once n > 70, the result gives only an approximation.

    Args:
        n (int): Position of the Fibonacci number to be returned. n must be greater than or 
        equal to 0.

    Returns:
        int: nth Fibonacci number.
    """
    num = math.pow(1 + math.sqrt(5), n) - math.pow(1 - math.sqrt(5), n)
    denom = math.pow(2, n) * math.sqrt(5)
    return round(num/denom)


print(fibonacci(22))
