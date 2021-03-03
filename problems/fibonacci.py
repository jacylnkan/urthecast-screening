import math

def fibonacci(n):
    phi = (math.sqrt(5) + 1)/2
    numerator = math.pow(phi, n) if n >= 0 else math.pow(-phi, -n)
    fib = round(numerator/math.sqrt(5))
    return fib

print(fibonacci(-3))

