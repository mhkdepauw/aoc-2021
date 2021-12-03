def file_to_list(filename):
    puzzle = open(filename, "r")
    list1 = puzzle.readlines()
    return list1

def main(filename):
    gamma_rate = ""
    epsilon_rate = ""
    list_of_file = file_to_list(filename)
    for i in range(12):
        if (bitchecker(list_of_file, i)) >= (len(list_of_file)/2):
            gamma_rate += "1"
            epsilon_rate += "0"
        else:
            gamma_rate += "0"
            epsilon_rate += "1"
    return int(gamma_rate, 2)*int(epsilon_rate, 2)


def bitchecker(list, place):
    one_count = 0
    for i in range(len(list)):
        if list[i][place] == "1":
            one_count += 1
    return one_count


print(main("puzzle3_input"))