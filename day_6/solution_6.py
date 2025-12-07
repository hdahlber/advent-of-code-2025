def read_in_file(filename="input.txt"):
    part_1_result = 0



    def part_2(lines,operations):
        part_2_result = 0
        cols = list(zip(*lines))
        groups =[]
        curr_group = []
        for col in cols:
            if set(col) == {" "}:
                groups.append(curr_group)
                curr_group = []
            else:
                digits = "".join(d for d in col if d != " ")
                curr_group.append(int(digits)) 
        
        if curr_group:
            groups.append(curr_group)
        
        for column, operation in zip(groups,operations):
            if operation == "*":
                result = 1
                for x in column:
                    result *= x
            elif operation == "+":
                result= 0
                for x in column:
                    result += x
    
            part_2_result += result
        return part_2_result

    with open(filename, "r") as file:
        lines = [line.strip("\n") for line in file.readlines()]
        
    #print(lines)
    operations = lines[-1]
    operations = operations.split()
    #print(operations)
    num_lines = lines[:-1]
    part_2_result =part_2(num_lines,operations)
    rows = []
    for line in num_lines:
        rows.append([int(x) for x in line.split()])
    cols = []
    for i in range(len(rows[0])):
        cols.append([row[i] for row in rows])
    #print(cols)
    for i,operation in enumerate(operations):
        column = cols[i]

        if operation == "*":
            result = 1
            for x in column:
                result *= x
        elif operation == "+":
            result= 0
            for x in column:
                result += x
        #print(result,column,operation)
        part_1_result += result
        

    return part_1_result, part_2_result

def main():
    part1_result,part2_result= read_in_file("input.txt")
    print(f"Part 1 results: {part1_result}")
    print(f"Part 2 results: {part2_result}")
if __name__ == "__main__":
    main()