
def read_in_file(filename="input.txt"):
    position = 50
    zeroes = 0
    passed_zero = 0
    with open(filename, "r") as file:
        for line in file:
            letter = line[0] 
            distance = int(line[1:])
            if letter == "R":
                passed_zero += (position + distance)//100
                position = (position + distance)%100
            elif letter == "L":
                flipped_position = (100 - position)%100
                passed_zero += (flipped_position + distance)//100
                position = (position - distance)% 100
            
            if position == 0:
                zeroes += 1
    
    return zeroes,passed_zero


def main():
    zeroes, passed_zero = read_in_file("input.txt")
    print(f"Part 1 results: {zeroes}")
    print(f"Part 2 results: {passed_zero}")
if __name__ == "__main__":
    main()