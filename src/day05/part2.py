"""
https://adventofcode.com/2023/day/5

>>> main(open("input_test.txt", "r"))
46
>>> main(open("input.txt", "r"))
31161857
"""

from utils import get_input_provider


def main(input_obj) -> None:
    def _traversing_backwards_to_seed(val: int) -> bool:
        current_val = val
        for map in maps[::-1]:
            for m in map:
                if current_val in range(m[0], m[0] + m[2]):
                    current_val = m[1] + current_val - m[0]
                    break
        return any([current_val in seed_range for seed_range in seed_ranges])

    maps = []
    seed_ranges = []
    for line in get_input_provider(input_obj):
        if not line:
            maps.append([])
            continue
        if "map" in line:
            continue

        if "seeds" in line:
            seeds = [int(i) for i in line.split(": ")[1].split()]
            for idx, r in enumerate(seeds):
                if idx % 2:
                    seed_ranges.append(range(seeds[idx - 1], seeds[idx - 1] + seeds[idx]))
        else:
            maps[-1].append([int(i) for i in line.split()])

    i = 0
    while True:
        if _traversing_backwards_to_seed(i):
            res = i
            break
        i += 1

    print(res)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
