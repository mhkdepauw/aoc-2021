

def make_file_list(filename):
    puzzle = open(filename, "r")
    list1 = puzzle.readlines()
    return list1


def sum_of_elements(col, number_list):
    return int(number_list[col - 2]) + int(number_list[col - 1]) + int(number_list[col])


def main():
    amount_of_increases = 0
    list_of_file = make_file_list("puzzle_input.txt")
    for i in range(len(list_of_file)):
        if (i-3) >= 0:
            if ((sum_of_elements(i - 1, list_of_file) - sum_of_elements(i, list_of_file))) < 0:
                amount_of_increases += 1
    return amount_of_increases


print(main())
