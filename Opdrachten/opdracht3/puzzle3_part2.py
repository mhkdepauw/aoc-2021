def file_to_list(filename):
    puzzle = open(filename, "r")
    global list1
    list1 = puzzle.readlines()
    return list1

def main(filename):
    list_of_file = file_to_list(filename)
    return int(list_sorter(list_of_file), 2)*int(other_list_sorter(file_to_list(filename)), 2)





def bitchecker(list, place):
    one_count = 0
    for i in range(len(list)):
        if list[i][place] == "1":
            one_count += 1
    return one_count
def bitchecker_zero(list, place):
    one_count = 0
    for i in range(len(list)):
        if list[i][place] == "0":
            one_count += 1
    return one_count


def list_sorter(list):
    for i in range(13):
        if len(list) != 1:
            new_list = oxygen_rating_calculator(list, i)
            list = new_list
        else:
            oxygen_rating = list[0]
            break
    return oxygen_rating


def oxygen_rating_calculator(list, place_bit):
    to_delete = []
    if bitchecker(list,place_bit) >= (len(list)/2):
        common_bit = "1"
        for j in range(len(list)):
            if list[j][place_bit] != common_bit:
                to_delete.append(list[j])
            else:
                pass
        for i in range(len(to_delete)):
            list.remove(to_delete[i])
    else:
        to_delete = []
        common_bit = "0"
        for j in range(len(list)):
            if list[j][place_bit] != common_bit:
                to_delete.append(list[j])
            else:
                pass
        for i in range(len(to_delete)):
            list.remove(to_delete[i])
    return list

def co2_rating_calculator(list, place_bit):
    to_delete = []
    if bitchecker_zero(list, place_bit) <= (len(list) / 2):
        common_bit = "0"
        for j in range(len(list)):
            if list[j][place_bit] != common_bit:
                to_delete.append(list[j])
            else:
                pass
        for i in range(len(to_delete)):
            list.remove(to_delete[i])
    else:
        to_delete = []
        common_bit = "1"
        for j in range(len(list)):
            if list[j][place_bit] != common_bit:
                to_delete.append(list[j])
            else:
                pass
        for i in range(len(to_delete)):
            list.remove(to_delete[i])
    return list

def other_list_sorter(list):
    for i in range(13):
        if len(list) != 1:
            new_list = co2_rating_calculator(list, i)
            list = new_list
        else:
            co2_rating = list[0]
            break
    return co2_rating



print(main("puzzle3_input"))