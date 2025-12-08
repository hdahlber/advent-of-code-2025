import networkx as nx
import math

def read_in_file(filename,end):
    part_1_result = 1
    part_2_result = 0
    nodes = []
    with open(filename) as file:
        input = file.read().splitlines()
    
    for line in input:
        parts = line.split(",")
        nums = tuple(int(x) for x in parts)
        nodes.append(nums)
    
    circuits = nx.Graph()
    circuits.add_nodes_from(nodes)

    #print(circuits)
    #print(nodes)
    distances = []
    for i in range(len(nodes)):
        for j in range(i+1,len(nodes)):
            a = nodes[i]
            b = nodes[j]
            distance = math.dist(a,b)
            distances.append((distance,a,b))
    distances.sort()
    
    for n in distances[:end]:
        circuits.add_edge(n[1],n[2])

    components = sorted(
        nx.connected_components(circuits),
        key=len,
        reverse=True
    )
    for x in components[:3]:
        #print(x)
        #print(len(x))
        part_1_result *= len(x)

    # part 2
    for n in distances[end:]:
        circuits.add_edge(n[1],n[2])
        if nx.is_connected(circuits):
            print(n[1][0])
            print(n[2][0])
            part_2_result = int(n[1][0]) * int((n[2][0]))
            break



    return part_1_result, part_2_result

def main():
    part1_result,part2_result= read_in_file("input.txt",1000)
    print(f"Part 1 results: {part1_result}")
    print(f"Part 2 results: {part2_result}")
if __name__ == "__main__":
    main()