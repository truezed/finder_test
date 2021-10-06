"""
Tests to check work with CLI.
"""

from random import randrange

import pytest
from nth_prime.tools import simple_parser


@pytest.fixture(name="parser")
def test_parser():
    """
    Fixture for creating simple parser.

    :return: Base args-parser for tests.
    """

    return simple_parser()


@pytest.mark.parametrize('number', [randrange(10000) for i in range(10)])
def test_correct_parsed(parser, number):
    """
    Test for checking the correctness of the arguments parser using the "--number" key.

    :param parser: Arguments parser for the test.
    :param number: The number for the test.
    """

    parsed = parser.parse_args(['--number', str(number)])
    assert parsed.number == number


@pytest.mark.parametrize('number', [randrange(10000) for j in range(10)])
def test_correct_parsed_short(parser, number):
    """
    Test for checking the correctness of the arguments parser using the "-n" key.

    :param parser: Arguments parser for the test.
    :param number: The number for the test.
    """

    parsed = parser.parse_args(['-n', str(number)])
    assert parsed.number == number
