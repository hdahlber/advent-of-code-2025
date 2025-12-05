
 
def read_in_file(filename="input.txt"):
    part_1_result = 0
    part_2_result = 0
    ranges = []
    merged = []
   

    
    with open(filename, "r") as file:

        for line in file:
            line = line.strip()

            if not line:
                continue
            
            if "-" in line:
                start, end = map(int, line.split("-"))
                ranges.append((start, end))

            else:
                ranges = sorted(ranges, key=lambda r: r[0])
                num = int(line)
                for start, end in ranges:
                    if start<=num <= end:
                        part_1_result += 1
                        break
                    
        for start,end in ranges: 
            if not merged or start > merged[-1][1]: # om inte i merged och start större än sista end
                
                merged.append([start, end])
            else:
                
                merged[-1][1] = max(merged[-1][1], end)

        for start,end in merged:
            part_2_result += end-start+1

                


    
    return part_1_result,part_2_result

def main():
    part1_result,part2_result= read_in_file("test.txt")
    print(f"Part 1 results: {part1_result}")
    print(f"Part 2 results: {part2_result}")
if __name__ == "__main__":
    main()