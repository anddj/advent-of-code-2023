"""
https://adventofcode.com/2023/day/3

>>> main("input_test.txt")
4361
>>> main("input.txt")
522726
"""

import re
from utils import get_input_provider


def main(filepath) -> None:
    buffer = []
    found_numbers = []

    pattern = re.compile(r"\d+")

    def _process_line(line):
        buffer.append(["."]+list(line)+["."])
        if not len(buffer) == 3:
            return

        found_numbers_local = []
        zipped_buffer = zip(*buffer)
        is_searching = True
        num_buf = []
        all_line_chars = ""
        for row in zipped_buffer:
            if row == (".", ".", ".") and not is_searching:
                if num_buf:
                    found_numbers_local.append(num_buf.copy())
                is_searching = True
                num_buf = []

            all_line_chars += row[1]
            if not is_searching:
                if row[0] == row[2] == "." and row[1].isnumeric():
                    num_buf.append(row[1])
                else:
                    is_searching = True
                    num_buf = []
                continue

            if row == (".", ".", "."):
                is_searching = False

        found_numbers_local = ["".join(n) for n in found_numbers_local]

        all_nums_found = pattern.findall(all_line_chars)
        for num in found_numbers_local:
            try:
                all_nums_found.remove(num)
            except ValueError:
                pass

        for x in all_nums_found:
            found_numbers.append(x)

        buffer.pop(0)

    line_length = 0
    for line in get_input_provider(filepath):
        if not buffer:
            line_length = len(line)
            buffer.append(["."]*line_length)
        _process_line(line)
    else:
        _process_line(["."]*line_length)

    print(sum(([int("".join(row)) for row in found_numbers])))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
