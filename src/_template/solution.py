"""
https://adventofcode.com/2023/day/N

>>> test_input_str = '''aaa
... bbb
... ccc'''
>>> main(test_input_str)
aaa
bbb
ccc
>>> main(open("input.txt", "r"))
input-line-1
input-line-2
input-line-3
"""

from utils import get_input_provider


def main(input_obj) -> None:
    for line in get_input_provider(input_obj):
        print(line)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
