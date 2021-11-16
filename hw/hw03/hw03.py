HW_SOURCE_FILE=__file__


def composer(func=lambda x: x):
    """
    Returns two functions -
    one holding the composed function so far, and another
    that can create further composed problems.
    >>> add_one = lambda x: x + 1
    >>> mul_two = lambda x: x * 2
    >>> f, func_adder = composer()
    >>> f1, func_adder = func_adder(add_one)
    >>> f1(3)
    4
    >>> f2, func_adder = func_adder(mul_two)
    >>> f2(3) # should be 1 + (2*3) = 7
    7
    >>> f3, func_adder = func_adder(add_one)
    >>> f3(3) # should be 1 + (2 * (3 + 1)) = 9
    9
    """

    def func_adder(g):
        """*** YOUR CODE HERE ***"""
        def compose1(f, g):
            return lambda x: f(g(x))
        return composer(compose1(func, g))

    return func, func_adder


def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
        return n
    else:
        return g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> # ban recursion
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
        return n
    else:
        present, one_before, two_before = 3, 2, 1
        for i in range(4, n + 1):
            one_before, two_before, three_before = present, one_before, two_before
            present = one_before + 2 * two_before + 3 * three_before
        return present



def missing_digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(35578) # 4, 6
    2
    >>> missing_digits(12456) # 3
    1
    >>> missing_digits(16789) # 2, 3, 4, 5
    4
    >>> missing_digits(19) # 2, 3, 4, 5, 6, 7, 8
    7
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if not n // 10:
        return 0
    else:
        last, second_last = n % 10, n // 10 % 10
        if last == second_last:
            return missing_digits(n // 10)
        else:
            return (last - second_last - 1) + missing_digits(n // 10)


def count_change(total, biggest_coin=None):
    """Return the number of ways to make change for total.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_change', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    def count_biggest_coin(total):
        """
        take TOTAL as the argument and return the biggest 2^n coin
        that is less than TOTAL
        """
        if total == 1:
            return 1
        else:
            return 2 * count_biggest_coin(total // 2)
        
    if total == 0:
        return 1
    if total < 0:
        return 0
    if biggest_coin == 1:
        return 1
    else:
        if biggest_coin == None:
            biggest_coin = count_biggest_coin(total)
        return count_change(total - biggest_coin, biggest_coin) + count_change(total, biggest_coin // 2)


def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"
    def choose_cache(start, end):
        """
        return the CACHE position by the given START position and END position.
        """
        for i in range(0, 3):
            if i+1 != start and i+1 != end:
                return i+1

    if n == 1:
        print_move(start, end)
    else:
        cache = choose_cache(start, end)
        move_stack(n - 1, start, cache)
        print_move(start, end)
        move_stack(n - 1, cache, end)



from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.
    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return (lambda f: lambda k: f(f, k))(lambda f, k: k if k == 1 else mul(k, f(f, sub(k, 1))))

def make_factorial():
    return something(nothing)
    # something == (lambda f: lambda k: f(f, k))
    # nothing = (lambda f, k: k if k == 1 else mul(k, f(f, sub(k, 1)))

def something(f):
    def otherthing(k):
        return f(f, k)
    return otherthing
def nothing(f, k):
    if k == 1:
        return k
    else:
        return mul(k, f(f, sub(k, 1)))

print(make_anonymous_factorial()(5))

# make_anonymous_factorial() == something(nothing) == (otherthing その中で f = nothing)
"""
make_anonymous_factorial()(5) = (otherthing(5) その中で f = nothing) == nothing(nothing, 5) == 5 * nothing(nothing, 4))
== 5 * 4 * nothing(nothing, 3) == 5 * 4 * 3 * nothing(nothing, 2) == 5 * 4 * 3 * 2 * nothing(nothing, 1) = 5 * 4 * 3 * 2 * 1
"""

