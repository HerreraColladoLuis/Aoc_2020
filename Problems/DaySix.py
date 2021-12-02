def solve_problem_1():
    input = open("C:\\AdventOfCode\\DaySix\\DaySixInput.txt", "r")
    i = 0
    list = input.readlines()
    total = 0
    while i < len(list):
        answers = ""
        while i < len(list) and list[i] != '\n':
            answers = answers + list[i][:-1]
            i = i + 1
        answers = "".join(set(answers))
        total = total + len(answers)
        i = i + 1

    return total


def solve_problem_2():
    input = open("C:\\AdventOfCode\\DaySix\\DaySixInput.txt", "r")
    i = 0
    lista = input.readlines()
    total = 0
    while i < len(lista):
        answers = set(list(lista[i][:-1]))
        i = i + 1
        while i < len(lista) and lista[i] != '\n':
            answers = answers & set(list(lista[i][:-1]))
            i = i + 1
        total = total + len(answers)
        i = i + 1

    return total


print(solve_problem_2())
