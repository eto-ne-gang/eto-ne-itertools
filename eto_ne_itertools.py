from typing import Generator


def count(start: int = 0, step: int = 1) -> Generator:
    """
    Returns an iterator of an infinite arithmetic sequence of integers
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
