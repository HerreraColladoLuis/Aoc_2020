def solve_problem_1():
    input = open("C:\\AdventOfCode\\DayFive\\DayFiveInput.txt", "r")
    highest = -1
    for line in input.readlines():
        row_ini = 0
        row_fin = 127
        col_ini = 0
        col_fin = 7
        row = 0
        col = 0
        i = 0
        while i < 6:
            if line[i] == 'F':
                row_fin = (row_ini + row_fin) // 2
            else:
                row_ini = row_ini + ((row_fin - row_ini) // 2) + 1
            i = i+1
        if line[6] == 'F':
            row = row_ini
        else:
            row = row_fin
        i = 7
        while i < 9:
            if line[i] == 'L':
                col_fin = (col_ini + col_fin) // 2
            else:
                col_ini = col_ini + ((col_fin - col_ini) // 2) + 1
            i = i+1
        if line[9] == 'L':
            col = col_ini
        else:
            col = col_fin

        id = row * 8 + col
        if id > highest:
            highest = id

    return highest


def do_seats_list():
    input = open("C:\\AdventOfCode\\DayFive\\DayFiveInput.txt", "r")
    seats_list = []
    for line in input.readlines():
        row_ini = 0
        row_fin = 127
        col_ini = 0
        col_fin = 7
        row = 0
        col = 0
        i = 0

        while i < 6:
            if line[i] == 'F':
                row_fin = (row_ini + row_fin) // 2
            else:
                row_ini = row_ini + ((row_fin - row_ini) // 2) + 1
            i = i + 1
        if line[6] == 'F':
            row = row_ini
        else:
            row = row_fin
        i = 7
        while i < 9:
            if line[i] == 'L':
                col_fin = (col_ini + col_fin) // 2
            else:
                col_ini = col_ini + ((col_fin - col_ini) // 2) + 1
            i = i + 1
        if line[9] == 'L':
            col = col_ini
        else:
            col = col_fin

        id = row * 8 + col
        seats_list.append(id)
    seats_list.sort()
    return seats_list


def solve_problem_2():
    seats_list = do_seats_list()
    i = 0
    while i < len(seats_list):
        if seats_list[i] + 1 != seats_list[i+1]:
            return seats_list[i] + 1
        i = i+1
    return 0


print(solve_problem_2())
