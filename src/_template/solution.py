"""
https://adventofcode.com/2023/day/N

>>> main("input.txt")
input-line-1
input-line-2
input-line-3
"""

from utils import get_input_provider


def main(filepath) -> None:
    for line in get_input_provider(filepath):
        print(line)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
