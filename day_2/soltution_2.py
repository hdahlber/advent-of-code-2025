def read_in_file(filename="input.txt"):
    part_1_result = 0
    part_2_result = 0

    def is_repating(s): # 121212
        n = len(s) # 6
        for size in range(1, n//2 + 1): # range(1,4)
            if n % size == 0: # 6%1, 6%2, 6%3
                pattern = s[:size] # 1,12,121
                if pattern * (n // size) == s: # size = 2 pattern ="12" n//size = 3  => if "12","12","12" == "121212"
                    return True
        return False

    with open(filename, "r") as file:
        line = file.read().strip()
        parts = line.strip().split(",")
        for p in parts:
            if p:  
                start, end = p.split('-')
            #print(f"Start: {start}, End: {end}")
            for i in range(int(start), int(end)+1):
                    s= str(i)
    
                    mid = len(s)//2
                    if (s[:mid] == s[mid:]):
                        print(f"Found matching halves:", {s[:mid]} ,{s[mid:]})
                        part_1_result += i
                    if is_repating(s):
                        print(f"Found repeating pattern:", {s})
                        part_2_result += i

    return part_1_result, part_2_result

def main():
    part1_result,part2_result= read_in_file("input.txt")
    print(f"Part 1 results: {part1_result}")
    print(f"Part 2 results: {part2_result}")
if __name__ == "__main__":
    main()