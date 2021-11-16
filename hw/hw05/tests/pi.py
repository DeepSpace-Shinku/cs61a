import math

def pi(n):
    assert n > 0 and isinstance(n, int), 'bad input'
    return 1 / (2 * math.sqrt(2) / 9801 * sum([math.factorial(4*k)*(1103+26390*k)/(math.factorial(k)**4*396**(4*k)) for k in range(n)]))


print(pi(3000))