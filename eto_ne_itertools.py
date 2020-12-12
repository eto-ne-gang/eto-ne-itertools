from typing import Generator, Iterable


def count(start: int = 0, step: int = 1) -> Generator:
    """
    Returns a generator of an infinite arithmetic sequence of integers
    with the first element equal to start and a certain step.

    :param start: the beginning number
    :param step: differnce between first and second element
    :return: generator of an infinite arithmetic sequence

    >>> counter = count(1, 5)
    >>> next(counter)
    1
    >>> next(counter)
    6
    >>> type(counter)
    <class 'generator'>
    """
    num = start

    while True:
        yield num
        num += step


def cycle(iterable: Iterable) -> Generator:
    """
    Returns an infinite generator over the
    content of the given iterable object.

    :param iterable: iterable object to create a cycle over
    :return: an infinite generator

    >>> cycle_1 = cycle("UCU")
    >>> next(cycle_1)
    'U'
    >>> next(cycle_1)
    'C'
    >>> next(cycle_1)
    'U'
    >>> type(cycle_1)
    <class 'generator'>
    """
    num = 0
    while True:
        yield iterable[num]

        num = (num + 1) % len(iterable)


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


def combinations(r: int, n: int) -> Generator:
    """
    Return a geenrator of combinations with unique elements of length
    r that consist of the first n integer values starting from 0.

    :param r: length of each combination
    :param n: number of integers to choose from

    >>> type(combinations(0, 4))
    <class 'generator'>
    >>> list(combinations(0, 4))
    [()]
    >>> list(combinations(5, 4))
    []
    >>> list(combinations(2, 3))
    [(0, 1), (0, 2), (1, 2)]
    """
    if r > n:
        return

    # generate the first combination
    nums = list(range(r))

    # return the first combination
    yield tuple(num for num in nums)

    while True:
        curr_idx = None

        # find index of rightmost element that can be modified
        for idx in reversed(range(r)):
            if nums[idx] != idx + n - r:
                curr_idx = idx
                break
        # if nothing can be modified, there is no more permutations
        else:
            return

        # increase the selected element by 1
        nums[curr_idx] += 1

        # for each element to the right from the selected one, switch it to
        # the smallest element that is currently possible at that position
        for idx in range(curr_idx + 1, r):
            nums[idx] = nums[idx - 1] + 1

        # return the current combination
        yield tuple(num for num in nums)


def combinations_with_replacement(r: int, n: int) -> Generator:
    """
    Return a geenrator of combinations with replacement of length
    r that consist of the first n integer values starting from 0.

    :param r: length of each combination
    :param n: number of integers to choose from

    >>> type(combinations_with_replacement(0, 4))
    <class 'generator'>
    >>> list(combinations_with_replacement(0, 4))
    [()]
    >>> list(combinations_with_replacement(5, 4))
    []
    >>> list(combinations_with_replacement(2, 3))
    [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]
    """
    if r > n:
        return

    # generate the first combination
    nums = [0] * r

    # return the first combination
    yield tuple(0 for _ in nums)

    while True:
        curr_idx = None

        # find index of rightmost element that can be modified
        for idx in reversed(range(r)):
            if nums[idx] != n - 1:
                curr_idx = idx
                break
        # if nothing can be modified, there is no more permutations
        else:
            return

        # increase the selected element by 1
        nums[curr_idx] += 1

        # for each element to the right from the selected one, switch it to
        # the smallest element that is currently possible at that position
        for idx in range(curr_idx + 1, r):
            nums[idx] = nums[idx - 1]

        # return the current combination
        yield tuple(num for num in nums)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
