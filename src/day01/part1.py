"""
https://adventofcode.com/2023/day/1

>>> test_input_str = '''1abc2
... pqr3stu8vwx
... a1b2c3d4e5f
... treb7uchet'''
>>> main(test_input_str)
142
>>> main()
55477
"""


from typing import Generator


def input_provider(input_str: str = None) -> Generator[str, None, None]:
    if input_str:
        for s in input_str.split("\n"):
            yield s
    else:
        with open("input.txt", "r") as f:
            for line in f:
                yield line.rstrip()


def main(input_str: str = None) -> None:
    answer: int = 0
    for line in input_provider(input_str):
        line_inputs = [line, reversed(line)]
        line_outputs = []
        for chars in line_inputs:
            for char in chars:
                if char.isdigit():
                    line_outputs.append(char)
                    break
        answer += int("".join(line_outputs))

    print(answer)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
