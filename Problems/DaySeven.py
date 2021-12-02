def to_dicc():
    input = open("C:\\AdventOfCode\\DaySeven\\DaySevenInput.txt", "r")
    item_list = {}
    for line in input.readlines():
        line_list = line.split(' ')
        if line_list[4] == "no":
            continue
        f_item = line_list[0] + line_list[1]
        i = 4
        while True:
            num = line_list[i]
            s_item = line_list[i+1]+line_list[i+2]
            if s_item not in item_list:
                item_list[s_item] = []
            item_list[s_item].append(f_item)
            if "." in line_list[i+3]:
                break
            i = i+4

    return item_list


def to_count(item_dicc, item_list, bag):
    cont = len(item_dicc[bag])
    for item in item_dicc[bag]:
        if item in item_list:
            cont = cont - 1
        else:
            item_list.append(item)
        if item in item_dicc:
            cont = cont + to_count(item_dicc, item_list, item)
    return cont


print(to_dicc())
print(to_count(to_dicc(), [], 'shinygold'))
