"""
https://adventofcode.com/2023/day/4

>>> test_input_str = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
... Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
... Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
... Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
... Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
... Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''
>>> main(test_input_str)
30
>>> main()
11787590
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
    cards = []
    for card_nr, line in enumerate(input_provider(input_str)):
        cards_info = line.split(":")
        winning_numbers, my_numbers = cards_info[1].split("|")
        winning_numbers, my_numbers = winning_numbers.split(), my_numbers.split()
        winning_numbers = set([int(i) for i in winning_numbers])
        my_numbers = set([int(i) for i in my_numbers])
        common_numbers = winning_numbers.intersection(my_numbers)
        try:
            # Count current card in
            cards[card_nr] += 1
        except IndexError:
            cards.append(1)
        for _ in range(cards[card_nr]):
            for i in range(len(common_numbers)):
                # Account card counters for copies down the line
                try:
                    cards[card_nr + 1 + i] += 1
                except IndexError:
                    cards.append(1)
    print(sum(cards))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
