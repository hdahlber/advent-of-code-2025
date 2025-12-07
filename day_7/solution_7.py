from collections import deque

def read_in_file(filename):
    part_1_result = 0
    part_2_result = 0
    splitters = set()
    file = open(filename,"r")
    input = file.read()
    file.close()
    

    lines = input.split("\n")
    rows = len(lines)
    matrix = []
    for line in lines:
        matrix.append([char for char in line])
    for line in matrix:
        print(line)
    col_start = ((0,matrix[0].index("S")))
    queue = deque([col_start])
    
    visited = set()
    while queue:
        row , col =  queue.popleft()
        #matrix[row][col] = "|"

        if (row,col) in visited:
            continue
        visited.add((row,col))

        new_row, new_col = row+1,col

        if new_row>= len(matrix) or new_col < 0 or new_col >= len(matrix[0]) :
            continue

    
        if new_row < rows-1:
            print(new_row,new_col,rows)
            if matrix[new_row][new_col] == ".":
                queue.append((new_row,new_col))
                matrix[new_row][new_col] = "|"
                continue
           



            if (new_row,new_col) not in splitters:
                splitters.add((new_row,new_col))
                matrix[new_row][new_col] = len(splitters)

            if (new_row,new_col+1) not in queue and new_col+1 < len(matrix[0]) and (new_row,new_col+1) not in visited: # oikea
                queue.append((new_row,new_col+1))
            if(new_row,new_col-1) not in queue and new_col-1 > -1 and (new_row,new_col-1) not in visited: #vasen
                 queue.append((new_row,new_col-1))

    print("----------")
    print(len(splitters))
    print(len(visited))
    print(splitters)
    print("----------")
    part_1_result = len(splitters)
        
        


        

    return part_1_result, part_2_result

def main():
    part1_result,part2_result= read_in_file("input.txt")
    print(f"Part 1 results: {part1_result}")
    print(f"Part 2 results: {part2_result}")
if __name__ == "__main__":
    main()