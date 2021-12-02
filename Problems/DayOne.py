def read_input():
    input = open("C:\\AdventOfCode\\DayOne\\DayOneInput.txt", "r")
    list = []
    for line in input.readlines():
        list.append(int(line))
    return list


def solve_problem_1(list):
    list.sort(reverse=True)
    fin = len(list)-1
    ini = 0
    while ini < fin:
        if list[ini]+list[fin] == 2020:
            return list[ini]*list[fin]
        elif list[ini]+list[fin] > 2020:
            ini = ini + 1
            fin = len(list)-1
        else:
            fin = fin-1
    return 0


def solve_problem_2(list):
    list.sort(reverse=True)
    fin = len(list)-1
    ini = 0
    inter = fin-1
    while ini < fin:
        if list[ini]+list[fin]+list[inter] == 2020:
            return list[ini]*list[fin]*list[inter]
        elif list[ini]+list[fin]+list[inter] > 2020:
            if inter == fin-1:
                ini = ini+1
                fin = len(list)-1
                inter = fin-1
            else:
                fin = fin-1
                inter = fin-1
        else:
            inter = inter-1
    return 0


print(solve_problem_2(read_input()))
