from scheme_reader import Pair, nil

def fcn(s):
    """
    >>> fcn(nil)
    ()
    >>> fcn(Pair(1, Pair(2, Pair(3, Pair(4, Pair(1, Pair(2, Pair(3, Pair(4, nil)))))))))
    Pair(Pair(1, Pair(2, Pair(3, Pair(4, nil)))), Pair(Pair(1, Pair(2, Pair(3, Pair(4, nil)))), nil))
    """
    if s is nil:
        return nil
    else:
        return Pair(longest_inc, Pair())


print(Pair(1, Pair(2, Pair(3, Pair(4, Pair(1, Pair(2, Pair(3, Pair(4, nil)))))))))
print(Pair(Pair(1, Pair(2, Pair(3, Pair(4, nil)))), Pair(Pair(1, Pair(2, Pair(3, Pair(4, nil)))), nil)))
