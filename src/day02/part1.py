"""
https://adventofcode.com/2023/day/2

>>> test_input_str = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
... Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
... Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
... Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
... Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''
>>> main(test_input_str)
8
>>> main()
2237
"""


import re
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
    bag_colors = {"red": 12, "green": 13, "blue": 14}
    pattern = re.compile("\\s(\\d+)\\s(\\w+)")
    game_ids_sum = 0
    for line in input_provider(input_str):
        game_info, game_sets = line.split(":")
        game_id = int(game_info.split()[1])
        game_sets = game_sets.split(";")
        for game_set in game_sets:
            game_set_stats = {"red": 0, "green": 0, "blue": 0}
            colors_info = game_set.split(',')
            for color_info in colors_info:
                parsed_color_info = pattern.search(color_info)
                game_set_stats[parsed_color_info[2]] = int(parsed_color_info[1])
            if (game_set_stats["red"] > bag_colors["red"] or
                game_set_stats["green"] > bag_colors["green"] or
                game_set_stats["blue"] > bag_colors["blue"]):
                    break
        else:
            game_ids_sum += game_id
    print(game_ids_sum)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
