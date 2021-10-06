"""
Module for package help functions.
"""

from argparse import ArgumentParser


def simple_parser() -> ArgumentParser:
    """
    Simple implementation of the CLI args parser.

    :return: ArgumentParser object.
    """
    arg_parser = ArgumentParser()
    arg_parser.add_argument('-n', '--number', type=int)

    return arg_parser
