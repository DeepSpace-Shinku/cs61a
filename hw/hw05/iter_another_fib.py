def long_fib(n):
    """
        >>> long_fib(3)
        1
        >>> long_fib(4)
        3
        >>> long_fib(5)
        5
        >>> long_fib(6)
        9
    """
    assert n > 0 and isinstance(n, int), 'bad input'
    if n <= 3:
        return 1
    else:
        pprev, prev, pre = 1, 1, 3
        ct = 4
        while ct < n:
            pprev, prev, pre = prev, pre, pprev+prev+pre
            ct += 1
        return pre

def cache_func_maker(func):
    cache = {}
    def cache_func(n):
        if not (n in cache):
            cache[n] = func(n)
        return cache[n]
    return cache_func

cache_long_fib = cache_func_maker(long_fib)

print([cache_long_fib(n+1) for n in range(100)])
print([long_fib(n+1) for n in range(100)])