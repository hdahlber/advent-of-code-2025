import re
from itertools import combinations 
def read_in_file(filename):
    part_1_result = 0
    part_2_result = 0
    with open(filename) as file:
        for line in file.read().splitlines():
            print(line)
            result = re.search(r'\[([.#]+)\]', line).group(0)
            num_buttons = re.findall(r'\([0-9,]*\)', line)
            jolts = re.search(r'\{([0-9,]+)\}', line).group(0)
            result = result.strip("[]")
            length = len(result)
            result = "".join("1" if x == "#" else "0" for x in result)
            result = int(result, 2) # bits to num so 0110 = 6
            buttons_bit = []
            
            for button in num_buttons:
                nums = [int(x) for x in button.strip("()").split(",") if x] # (0,2) => ["0","2"]
                mask = 0
                for n in nums:
                    bit_index = length - n - 1
                    mask |= 1 << bit_index # bitwise left 
                buttons_bit.append(mask)
            #print(buttons_bit)
            B = len(buttons_bit)
            for r in range(B+1):
                for combo in combinations(range(B),r):
                    state = 0
                    for index in combo:
                        state ^= buttons_bit[index]  

                    if state == result:
                        part_1_result += r
                        break
                else:
                    continue
                break


            
    
    


    return part_1_result, part_2_result

def main():
    part1_result,part2_result= read_in_file("test.txt")
    print(f"Part 1 results: {part1_result}")
    print(f"Part 2 results: {part2_result}")
if __name__ == "__main__":
    main()