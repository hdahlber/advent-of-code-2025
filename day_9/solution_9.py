def read_in_file(filename):
    part_1_result = 0
    part_2_result = 0
    nodes = []
    with open(filename) as file:
        input = file.read().splitlines()
    
    for line in input:
        parts = line.split(",")
        nums = tuple(int(x) for x in parts)
        nodes.append(nums)
    nodes.sort(key=lambda x: x[0], reverse=True)
    #print(nodes)
    
    for i in range(len(nodes)):
        for j in range(i+1,len(nodes)):
            print(nodes[i],nodes[j])
            y_axis = nodes[i][0]-nodes[j][0]+1
            x_axis = abs(nodes[i][1]-nodes[j][1])+1
            size = y_axis*x_axis
            if size > part_1_result:
                #print(y_axis,x_axis, nodes[i],nodes[j])
                part_1_result= size
    
    


    return part_1_result, part_2_result

def main():
    part1_result,part2_result= read_in_file("test.txt")
    print(f"Part 1 results: {part1_result}")
    print(f"Part 2 results: {part2_result}")
if __name__ == "__main__":
    main()