def file_to_list(filename):
    puzzle = open(filename, "r")
    list1 = puzzle.readlines()
    return list1

def main():
    horizontal_position = 0
    aim = 0
    depth = 0
    list_of_file = file_to_list("input_puzzle2")
    for i in range((len(list_of_file))):
        if "down" in list_of_file[i]:
            aim += int(list_of_file[i][-2])
        elif "forward" in list_of_file[i]:
            horizontal_position += int(list_of_file[i][-2])
            depth += aim*int(list_of_file[i][-2])
        else:
            aim -= int(list_of_file[i][-2])
    return horizontal_position * depth

print(main())