"""
https://adventofcode.com/2023/day/8

>>> main("input_test3.txt")
6
>>> main("input.txt")
7309459565207
"""

import itertools
from math import lcm
from utils import get_input_provider


def main(input_obj) -> None:
    nodes_raw_data = {}
    nodes_traverse_schema = None
    for line in get_input_provider(input_obj):
        if "=" in line:
            members = line.split("=")
            left, right = members[1].split(", ")
            left = left[2:]
            right = right[:-1]
            nodes_raw_data[members[0].strip()] = (left, right)
        elif line:
            nodes_traverse_schema = line.strip()

    start_nodes = [ k for k in nodes_raw_data.keys() if k.endswith("A") ]

    direction_index = {"L": 0, "R": 1}
    counters = []
    for start_node in start_nodes:
        current_node = start_node
        counter = 0
        for direction in itertools.cycle(nodes_traverse_schema):
            counter += 1
            next_node = nodes_raw_data[current_node][direction_index[direction]]
            if next_node.endswith("Z"):
                counters.append(counter)
                break
            current_node = next_node

    answer = lcm(*counters) # least common multiple of all counters

    print(answer)



if __name__ == "__main__":
    import doctest
    doctest.testmod()
