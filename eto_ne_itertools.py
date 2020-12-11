'''
This module implements equivalent realisation of itertools
repeat and product functions
'''

def repeat(val, num=False):
    '''
    iterator that returns object either infinite amount
    of times or a specified amount of times
    >>> list(map(pow, range(10), repeat(2)))
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    >>> list(repeat(100, 10))
    [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
    >>> list(repeat('spam', 5))
    ['spam', 'spam', 'spam', 'spam', 'spam']
    '''

    if not num:
        while True:
            yield val
    else:
        for _ in range(num):
            yield val


def product(*iterables, repeat=1):
    '''
    Function returns cartesian product of input iterables
    >>> list(product([1,2], range(2), 'ab'))
    [(1, 0, 'a'), (1, 0, 'b'), (1, 1, 'a'), (1, 1, 'b'), (2, 0, 'a'),\
 (2, 0, 'b'), (2, 1, 'a'), (2, 1, 'b')]
    >>> list(product([1,2,3], [4,5,6]))
    [(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]
    '''

    iter_lst = [list(iter_var) for iter_var in iterables] * repeat
    result = [[]]
    for iter_var in iter_lst:
        result = [x+[y] for x in result for y in iter_var]
    for prod in result:
        yield tuple(prod)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
