def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    res = 1
    for i in range (n, n - k, -1):
        res *= i
    return res

#print(falling(6, 3))  # 6 * 5 * 4


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    res = 0
    while y:
        digit = y % 10
        res += digit
        y //= 10
    return res

#print(sum_digits(1234567890))



def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    con = False # 0 means the previous digit of the number is not 8, else it means the previous digit is 8
    while n:
        if n % 10 == 8 and con:
            return True
        elif n % 10 == 8:
            con = True
        else:
            con = False
        n //= 10
    return False

#print(double_eights(8), double_eights(88), double_eights(2882), double_eights(880088), double_eights(12345), double_eights(80808080))




