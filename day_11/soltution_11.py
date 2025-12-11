import networkx as nx
import math
from functools import cache

def read_in_file(filename):
    part_1_result = 0
    part_2_result = 0
    circuits = nx.DiGraph()
    required_nodes = set(["fft", "dac"])
    
    with open(filename) as file:
        for line in file:
            node , children = line.split(":")
            node = node.strip()
            targets = children.strip().split()

            circuits.add_node(node)

            for child in targets:
                circuits.add_node(child)
                circuits.add_edge(node,child)

    #part_1_result= (len(list(nx.all_simple_paths(circuits, source="you", target="out"))))

    @cache
    def count_paths(curr, visited_required=frozenset()):

       
        new_visited = visited_required | (required_nodes & {curr})


        if curr == "out":
            return 1 if new_visited == required_nodes else 0

        total = 0
        for nxt in circuits.neighbors(curr):
            total += count_paths(nxt, new_visited)
        return total


    part_2_result = count_paths("svr")

    

    return part_1_result, part_2_result

def main():
    part1_result,part2_result= read_in_file("input.txt")
    print(f"Part 1 results: {part1_result}")
    print(f"Part 2 results: {part2_result}")
if __name__ == "__main__":
    main()