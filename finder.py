from nth_prime.tools import simple_parser
from nth_prime import get_nth_prime


def run():
    parser = simple_parser()
    print(get_nth_prime(parser.parse_args().number))


if __name__ == '__main__':
    run()
