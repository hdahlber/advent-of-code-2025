from functools import reduce
from operator import add

 
def read_in_file(filename="input.txt"):
    part_1_result = 0
    part_2_result = 0
   

    def part_1(line):
        result = 0
        line = line.strip()
        list =line[:]
        num_1 = -1
        num_2 = int(list[-1])
        #print("start",num_1,num_2, list)
        #part 1
        for i in range(2, len(list)+1):
            #print("checking",list[-i], num_1, num_2)
            if int(list[-i]) >= num_1: # om nya större än gamla first number
                if num_1 >= num_2:
                    num_2 = num_1
                    num_1 = int(list[-i])
                else:
                    num_1 = int(list[-i])
                
            
        #print("end",num_1,num_2, list)
        #int(reduce(add,map(str, [num_1, num_2])))
        result += int(str(num_1)+str(num_2))
        return result
    
    def part_2(line,index_number,check):
        placeholder_index = 0
        number = 0
        
        #print(index_number, check)


        for i in range(check - 1, index_number, -1):
            #print(i)
            if int(line[i]) >= number:
                #print("New number found:", line[i], "at index", i)
                number = int(line[i])
                placeholder_index = i
        index_number = placeholder_index
        return number,index_number

            

    with open(filename, "r") as file:
        for line in file:
            part_1_result += part_1(line)
            list_part_2 = []
            index_number = -1
            check = len(line.strip()) - 11
            for i in range(0,12):
               # print("Round:", i)
                reslut_part, index_number = part_2(line, index_number, check)
                check = check+1
                list_part_2.append(reslut_part)
                #print(reslut_part, index_number)
            #print(int(reduce(add,map(str, list_part_2))))
            part_2_result += int(reduce(add,map(str, list_part_2)))
            
    return part_1_result, part_2_result

def main():
    part1_result,part2_result= read_in_file("input.txt")
    print(f"Part 1 results: {part1_result}")
    print(f"Part 2 results: {part2_result}")
if __name__ == "__main__":
    main()