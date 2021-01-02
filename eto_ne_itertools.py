"""A module with alternatives of some functions from itertools module.

    Functions
    ---------
        count - an infinite arithmetic sequence
        cycle - an infinite cycle over the iterable object
        repeat - repetition of a value
        product - cartesian product of input iterables
        combinations - combinations of certain length with unique elements
        combinations_with_replacement - combinations of certain length with
                                        unique elements that might contain duplicates
        permutations - permutations of certain length with unique elements

"""
from typing import Generator, Iterable


def count(start: int = 0, step: int = 1) -> Generator:
    """
    Returns a generator of an infinite arithmetic sequence of integers
    with the first element equal to start and a certain step.

    :param start: the beginning number
    :param step: difference between first and second element
    :return: generator of an infinite arithmetic sequence


    >>> counter = count(1, 5)
    >>> type(counter)
    <class 'generator'>
    >>> next(counter)
    1
    >>> next(counter)
    6
    >>> counter = count()
    >>> next(counter)
    0
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
    >>> type(cycle_1)
    <class 'generator'>
    >>> next(cycle_1)
    'U'
    >>> next(cycle_1)
    'C'
    >>> next(cycle_1)
    'U'
    """
    num = 0
    while True:
        yield iterable[num]

        num = (num + 1) % len(iterable)


def repeat(val):
    '''
    Return a generator of repeated value.Default
    number of repetitions equals to infinity.

    :param val: a value to repeat
    :param repeat[optional]: number of repetitions
    :return: generator of repeated values

    >>> type(repeat(5, 10))
    <class 'generator'>
    >>> list(repeat([1,2,3], 4))
    [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]
    >>> list(repeat(100, 10))
    [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
    >>> list(repeat('Hello World!', 3))
    ['Hello World!', 'Hello World!', 'Hello World!']
    '''

    # if the amount of repeats is not given - return generator infinitely
    if not num:
        while True:
            yield val

    # return generator of the value given amount of times
    for _ in range(num):
        yield val


def product(*iterables: Iterable, repeat: int = 1):
    '''
    Return a generator with a cartesian product of given iterables.

    :param iterables: iterable objects
    :param repeat[optional]: number of repetitions
    :return: generator of cartesian product

    >>> list(product([1,2], range(2), 'ab'))
    [(1, 0, 'a'), (1, 0, 'b'), (1, 1, 'a'), (1, 1, 'b'), (2, 0, 'a'),\
 (2, 0, 'b'), (2, 1, 'a'), (2, 1, 'b')]
    >>> list(product([1,2,3], [4,5,6]))
    [(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]
    >>> list(product(('Hello', 1), [2, 'World!']))
    [('Hello', 2), ('Hello', 'World!'), (1, 2), (1, 'World!')]
    '''

    # read all the iterables as list, write down each in list
    all_iterables = []

    for iterable in iterables:
        iterable = list(iterable)
        all_iterables.append(iterable)

    all_iterables *= repeat

    result = [[]]

    # operate each iterable and find cartesian product for them
    for iterable in all_iterables:
        cartesian = []

        # get sublists of result and find cartesian product for
        # currently operated iterables
        for temp_result_lst in result:

            # add to each list present in result elements of new iterable
            for element in iterable:
                copy_res_lst = temp_result_lst
                copy_res_lst = copy_res_lst + [element]
                cartesian.append(copy_res_lst)

        result = cartesian

    # form elements of cartesian product as tuples instead of lists
    for prod in result:
        yield tuple(prod)


def combinations(r: int, n: int) -> Generator:
    """
    Return a generator of combinations with unique elements of length
    r that consist of the first n integer values starting from 0.

    :param r: length of each combination
    :param n: number of integers to choose from
    :return: generator of combionations

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
    yield tuple(nums)

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
    Return a generator of combinations with replacement of length
    r that consist of the first n integer values starting from 0.

    :param r: length of each combination
    :param n: number of integers to choose from
    :return: generator of combionations with replacement

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
        

def permutations(iterable, length="iterable"):
    """
    Recursively generates k-permutations of an iterable.
    Yields a new permutation (in ascending order) with each next() call.
    If length is not specified, it is set to the length of the iterable.
    Returns an iterable of all permutations.

    :param iterable: iterable to get permutations from
    :param length: length of each permutation
    :return: generator object (iterable of all permutations found)

    >>> list(permutations([1,2,3], 2))
    [[1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2]]
    >>> list(permutations([10, 16, -11], 3))
    [[10, 16, -11], [10, -11, 16], [16, 10, -11], [16, -11, 10], [-11, 10, 16], [-11, 16, 10]]
    >>> list(permutations([1,5,-7]))
    [[1, 5, -7], [1, -7, 5], [5, 1, -7], [5, -7, 1], [-7, 1, 5], [-7, 5, 1]]
    >>> type(permutations([1, 2, 3]))
    <class 'generator'>
    """
    if length == "iterable":
        length = len(iterable)
    if length == 1:
        lst = [[el] for el in iterable]
        for permutation in lst:
            yield permutation
    else:
        new_permutations = []
        for permutation in permutations(iterable, length - 1):
            temp_iterable = []
            for elem in iterable:
                if elem not in permutation:
                    temp_iterable.append(elem)
            for add_elem in temp_iterable:
                new_permutations.append(permutation + [add_elem])
        for permutation in new_permutations:
            yield permutation




if __name__ == '__main__':
    import doctest
    doctest.testmod()
