"""
https://adventofcode.com/2023/day/1

>>> test_input_str = '''two1nine
... eightwothree
... abcone2threexyz
... xtwone3four
... 4nineeightseven2
... zoneight234
... 7pqrstsixteen'''
>>> main(test_input_str)
281
>>> main()
54431
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


def string_to_arabic(string: str) -> str or None:
    # Look for the number name in the string and return the corresponding arabic number
    numbers_map: dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven":"7",
        "eight": "8",
        "nine": "9",
    }
    for key in numbers_map.keys():
        if key in string:
            return numbers_map[key]
    return None

def main(input_str: str = None) -> None:
    answer: int = 0
    for line in input_provider(input_str):
        line_inputs = [line, reversed(line)]
        line_outputs = []
        for idx, chars in enumerate(line_inputs):
            current_number_as_string: str = ""
            for char in chars:
                if char.isdigit():
                    line_outputs.append(char)
                    break
                else:
                    current_number_as_string += char
                    if idx == 0:
                        number = string_to_arabic(current_number_as_string)
                    else:
                        number = string_to_arabic(current_number_as_string[::-1])
                    if number is not None:
                        line_outputs.append(number)
                        break
        answer += int("".join(line_outputs))

    print(answer)




if __name__ == "__main__":
    import doctest
    doctest.testmod()
