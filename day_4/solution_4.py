
 
def read_in_file(filename="input.txt"):
    part_1_result = 0
    part_2_result = 0
   
    def part_1(combined,symbols_per_line,num_lines):
        result = 0
        new_string = ""
        neighbors = [-1, +1,-symbols_per_line, -symbols_per_line-1, -symbols_per_line+1,+symbols_per_line, +symbols_per_line-1, +symbols_per_line+1]

        for x in range(len(combined)):
            if combined[x] != "@":
                new_string += "H"
                continue
            count = 0
            for offset in neighbors:
                if offset in (-1, -symbols_per_line-1, +symbols_per_line-1) and x % symbols_per_line == 0:
                    continue 
                if offset in (+1, -symbols_per_line+1, +symbols_per_line+1) and x % symbols_per_line == symbols_per_line - 1:
                    continue

                n = x + offset
                if 0 <= n < len(combined) and combined[n] == "@":
                    count += 1
                    

            if count < 4:
                result += 1
                new_string += "H"
            else:
                new_string += combined[x]


        return result,new_string
        
                        

        return result
    with open(filename, "r") as file:
        lines = [line.strip() for line in file]
        num_lines = len(lines)
        combined = "".join(lines)
        symbols_per_line = int(len(combined)/num_lines)
        part_1_result,new_string= part_1(combined,symbols_per_line,num_lines)
        part_2_result += part_1_result
        que = True
        while que:
            print("start")
            result,new_string = part_1(new_string,symbols_per_line,num_lines)
            print(new_string)
            print("result",result)
            if result == 0:
                que = False
            else:
                part_2_result += result

    
        return part_1_result,part_2_result

def main():
    part1_result,part2_result= read_in_file("input.txt")
    print(f"Part 1 results: {part1_result}")
    print(f"Part 2 results: {part2_result}")
if __name__ == "__main__":
    main()