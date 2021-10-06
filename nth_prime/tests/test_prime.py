"""
Tests to check basic functionality.
"""

from random import randrange

import pytest
from nth_prime.prime import is_prime, get_nth_prime


IS_PRIME_VALUES = [
    (0, False), (5, True), (40, False), (443, True), (1103, True),
    (1723, True), (2690, False), (446, False), (3593, True),
    (584, False), (5009, True), (5843, True), (6600, False),
    (6841, True), (928, False), (7507, True), (7674, False),
    (7919, True), (133584, False), (291089, True)
]

# https://en.wikipedia.org/wiki/List_of_prime_numbers
# https://primes.utm.edu/nthprime/index.php
NTH_PRIME_VALUES = [
    (0, 0), (3, 5), (13, 41), (86, 443), (185, 1103),
    (269, 1723), (392, 2693), (446, 3137), (503, 3593),
    (584, 4259), (671, 5009), (767, 5843), (853, 6599),
    (881, 6841), (928, 7253), (951, 7507), (973, 7673),
    (1000, 7919), (12464, 133583), (25315, 291089)
]


@pytest.mark.parametrize(('number', 'expected'), IS_PRIME_VALUES)
def test_is_prime(number, expected):
    """
    A test to verify the correctness of the definition of prime numbers.

    :param number: The number for the test.
    :param expected: Expected answer.
    """

    assert is_prime(number) == expected


@pytest.mark.parametrize(('number', 'expected'), NTH_PRIME_VALUES)
def test_nth_prime(number, expected):
    """
    A test for verifying the correctness of the definition of the nth prime number.

    :param number: The number for the test.
    :param expected: Expected answer.
    """

    assert get_nth_prime(number) == expected


@pytest.mark.parametrize('number', [-randrange(1, 10000) for i in range(10)])
def test_negative_number(number):
    """
    A test to verify that it works correctly with negative numbers.

    :param number: The number for the test.
    """

    assert get_nth_prime(number) == 0
