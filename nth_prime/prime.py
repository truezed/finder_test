"""
A module with the main functionality of the package.
"""


def is_prime(number: int) -> bool:
    """
    Function for checking a number for prime.

    :param number: Number to check for prime.
    :return: True if prime, otherwise False.
    """

    if number in (2, 3):
        return True
    if number < 2:
        return False
    if number % 2 == 0 or number % 3 == 0:
        return False
    if number < 9:
        return True

    i = 5
    while i <= int(number ** 0.5):
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6

    return True


def get_nth_prime(number: int) -> int:
    """
    Function for getting the nth prime number.

    :param number: Nth.
    :return: Nth prime value.
    """

    if not number or number < 0:
        return 0

    if not isinstance(number, int):
        number = int(number)

    nth_prime = 1
    result_prime = 2
    current_prime = 2
    while nth_prime <= number:
        if is_prime(current_prime):
            result_prime = current_prime
            nth_prime += 1
        current_prime += 1

    return result_prime
