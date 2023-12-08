"""
https://adventofcode.com/2023/day/8

>>> main("input_test.txt")
2
>>> main("input_test2.txt")
6
>>> main("input.txt")
13301
"""

from utils import get_input_provider

class Node:
    def __init__(self, name=None):
        self.name = name
        self.left = None
        self.right = None

class LinkedNodes:
    def __init__(self):
        self.head = None

    def traverse_nodes(self, nodes_traverse_schema):
        node = self.head
        directions_map = {
            "L": "left",
            "R": "right"
        }
        steps = 0
        found = False
        answer = None
        while True:
            if found:
                break
            for direction in nodes_traverse_schema:
                steps += 1
                node = getattr(node, directions_map[direction])
                if node.name == "ZZZ":
                    answer = steps
                    found = True
                    break

        print(answer)


def main(input_obj) -> None:

    nodes_data = {}
    for line in get_input_provider(input_obj):
        if "=" in line:
            members = line.split("=")
            left, right = members[1].split(", ")
            left = left[2:]
            right = right[0:-1]
            nodes_data[members[0].strip()] = (left, right)
        elif line:
            nodes_traverse_schema = line.strip()

    nodes_dict = {}
    for key, value in list(nodes_data.items())[::-1]:
        node = Node(key)
        if key in nodes_dict:
            node = nodes_dict[key]
        else:
            nodes_dict[key] = node

        if value[0] != key:
            if value[0] in nodes_dict:
                node.left = nodes_dict[value[0]]
            else:
                nodes_dict[value[0]] = Node(value[0])
                node.left = nodes_dict[value[0]]

        if value[1] != key:
            if value[1] in nodes_dict:
                node.right = nodes_dict[value[1]]
            else:
                nodes_dict[value[1]] = Node(value[1])
                node.right = nodes_dict[value[1]]

    head_node = nodes_dict["AAA"]

    nodes_list = LinkedNodes()
    nodes_list.head = head_node
    nodes_list.traverse_nodes(nodes_traverse_schema)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
