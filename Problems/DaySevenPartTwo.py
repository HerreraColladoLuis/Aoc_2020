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
            if f_item not in item_list:
                item_list[f_item] = []
            item_list[f_item].append((s_item, num))
            if "." in line_list[i+3]:
                break
            i = i+4

    return item_list


def to_count(item_dicc, bag):
    cont = 0
    for item in item_dicc[bag]:
        if item[0] in item_dicc:
            cont = cont + int(item[1]) + int(item[1]) * to_count(item_dicc, item[0])
        else:
            cont = cont + int(item[1])
    return cont


#print(to_dicc())
print(to_count(to_dicc(), 'shinygold'))
