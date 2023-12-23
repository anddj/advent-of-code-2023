"""
https://adventofcode.com/2023/day/3

>>> main("input_test.txt")
467835
>>> main("input.txt")
81721933
"""

import re
from utils import get_input_provider


def main(filepath) -> None:
    buffer = []
    line_length = 0
    pattern = re.compile(r"\d+")
    answer = 0

    def _process_line(line):
        res = 0
        buffer.append("."+line+".")
        if not len(buffer) == 3:
            return 0

        number_positions = []
        for buf in buffer:
            matches = pattern.finditer(buf)
            number_positions.append([(match.start(), match.end()) for match in matches])
        star_positions = [i for i, c in enumerate(buffer[1]) if c == '*']

        for star_position in star_positions:
            temp_buf = []
            for buffer_nr, num_position in enumerate(number_positions):
                for start, end in num_position:
                    if start-1 <= star_position <= end:
                        temp_buf.append(buffer[buffer_nr][start:end])
            if len(temp_buf) == 2:
                res += int(temp_buf[0])*int(temp_buf[1])

        buffer.pop(0)
        return res

    for line in get_input_provider(filepath):
        if not buffer:
            line_length = len(line)
            buffer.append("."*line_length)
        answer += _process_line(line)
    else:
        answer += _process_line("."*line_length)

    print(answer)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
