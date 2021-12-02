

def file_to_list(filename):
    puzzle = open(filename, "r")
    list1 = puzzle.readlines()
    return list1



def main():
    amount_of_increases = 0
    list_of_file = file_to_list("puzzle_input.txt")
    for i in range(len(list_of_file)):
        if (i-1) >= 0:
            if (int(list_of_file[i-1]) - int(list_of_file[i])) < 0:
                amount_of_increases += 1
    return amount_of_increases

print(main())