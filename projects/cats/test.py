"""
def printer(n):
    """
"""
    print the sequence from 1 to n to 1 in a recursive way.

    >>> printer(4)
    1 2 3 4 3 2 1
    >>> printer(1)
    1
    >>> printer(2)
    1 2 1
    >>> printer(3)
    1 2 3 2 1
    """
"""
    def sequence_maker(m, cond='beginning'):
        if m == 1:
            print(1, end='')
            if cond == 'increment':
                print('', end=' ')
        else:
            if cond == 'beginning':
                sequence_maker(m-1, 'increment')
                print(m, end=' ')
                sequence_maker(m-1, 'decrement')
            else:
                if cond == 'increment':
                    sequence_maker(m-1, cond='increment')
                    print(m, end=' ')
                elif cond == 'decrement':
                    print(m, end=' ')
                    sequence_maker(m - 1, cond='decrement')
    sequence_maker(n)"""
    #######################################
    #### The code above is too complex ####
    #######################################


def printer(n):
    """
    print the sequence from 1 to n to 1 in a recursive way.

    
    >>> printer(4)
    1 2 3 4 3 2 1
    >>> printer(1)
    1
    >>> printer(2)
    1 2 1
    >>> printer(3)
    1 2 3 2 1
    """
    def sequence_maker(m):
        if m == n:
            print(n, end='')
            if n != 1:
                print(' ', end='')
        elif not m > n:
            print(m, end=' ')
            sequence_maker(m+1)
            print(m, end='')
            if m != 1:
                print(' ', end='')
    sequence_maker(1)