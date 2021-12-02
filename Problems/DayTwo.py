def solve_problem_1():
    input = open("C:\\AdventOfCode\\DayTwo\\DayTwoInput.txt", "r")
    out = 0
    for line in input.readlines():
        line = line.split(" ")
        ini_list = line[0].split("-")
        ini = int(ini_list[0])
        fin = int(ini_list[1])
        lett = line[1][:-1]
        pwd = line[2]
        cont = 0
        for c in pwd:
            if c == lett:
                cont = cont+1
        if cont >= ini:
            if cont <= fin:
                out = out+1
    return out


def solve_problem_2():
    input = open("C:\\AdventOfCode\\DayTwo\\DayTwoInput.txt", "r")
    out = 0
    for line in input.readlines():
        line = line.split(" ")
        ini_list = line[0].split("-")
        ini = int(ini_list[0])
        fin = int(ini_list[1])
        lett = line[1][:-1]
        pwd = line[2]

        if pwd[ini-1] == lett and pwd[fin-1] != lett:
            out = out+1
        elif pwd[ini-1] != lett and pwd[fin-1] == lett:
            out = out+1
    return out


print(solve_problem_2())
