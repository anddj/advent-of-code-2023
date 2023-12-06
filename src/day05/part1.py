"""
https://adventofcode.com/2023/day/N

>>> main(open("input_test.txt", "r"))
35
>>> main(open("input.txt", "r"))
57075758
"""

from utils import get_input_provider

seeds = []
maps = {
    "seed-to-soil map": [],
    "soil-to-fertilizer map": [],
    "fertilizer-to-water map": [],
    "water-to-light map": [],
    "light-to-temperature map": [],
    "temperature-to-humidity map": [],
    "humidity-to-location map": [],
}

def get_location(val: int) -> int:
    current_val = val
    for key, named_maps in maps.items():
        for map in named_maps:
            if map[1] <= current_val < map[1] + map[2]:
                current_val = map[0] + current_val - map[1]
                break
    return current_val

def main(input_obj) -> None:
    parse_mode = None
    for line in get_input_provider(input_obj):
        line_data = line.split(":")
        if len(line_data) == 2:
            parse_mode = line_data[0]
            if parse_mode == "seeds":
                seeds = [int(i) for i in line_data[1].split()]
        elif line_data[0] != "":
            maps[parse_mode].append([int(i) for i in line_data[0].split()])

    print(min([get_location(seed) for seed in seeds]))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
