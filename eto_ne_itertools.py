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
