def read_input():
    input = open("C:\\AdventOfCode\\DayThree\\DayThreeInput.txt", "r")
    list = []
    for line in input.readlines():
        list.append(line[:-1])
    return list


def solve_problem_1(map):
    trees = 0
    pos = 0
    for i in range(len(map)):
        if i+2 > len(map):
            return trees
        else:
            if pos+1 == len(map[i]):  #..#..#.[.]
                pos = 2
                if map[i + 1][pos] == "#":
                    trees = trees + 1
                continue
            elif pos+2 == len(map[i]):  #..#..#[.].
                pos = 1
                if map[i + 1][pos] == "#":
                    trees = trees + 1
                continue
            elif pos+3 == len(map[i]):  #..#..[#]..
                pos = 0
                if map[i + 1][pos] == "#":
                    trees = trees + 1
                continue
            else:
                if map[i+1][pos+3] == "#":
                    trees = trees+1
            pos = pos+3


def solve_problem_2_1(map):
    trees = 0
    pos = 0
    for i in range(len(map)):
        if i+2 > len(map):
            return trees
        else:
            if pos+1 == len(map[i]):  #..#..#.[.]
                pos = 0
                if map[i + 1][pos] == "#":
                    trees = trees + 1
                continue
            else:
                if map[i+1][pos+1] == "#":
                    trees = trees+1
            pos = pos+1


def solve_problem_2_2(map):
    trees = 0
    pos = 0
    for i in range(len(map)):
        if i+2 > len(map):
            return trees
        else:
            if pos+1 == len(map[i]):  #..#..#.[.]
                pos = 4
                if map[i + 1][pos] == "#":
                    trees = trees + 1
                continue
            elif pos+2 == len(map[i]):  #..#..#[.].
                pos = 3
                if map[i + 1][pos] == "#":
                    trees = trees + 1
                continue
            elif pos+3 == len(map[i]):  #..#..[#]..
                pos = 2
                if map[i + 1][pos] == "#":
                    trees = trees + 1
                continue
            elif pos+4 == len(map[i]):  #..#.[.]#..
                pos = 1
                if map[i + 1][pos] == "#":
                    trees = trees + 1
                continue
            elif pos+5 == len(map[i]):  #..#[.].#..
                pos = 0
                if map[i + 1][pos] == "#":
                    trees = trees + 1
                continue
            else:
                if map[i+1][pos+5] == "#":
                    trees = trees+1
            pos = pos+5


def solve_problem_2_3(map):
    trees = 0
    pos = 0
    for i in range(len(map)):
        if i+2 > len(map):
            return trees
        else:
            if pos+1 == len(map[i]):  #..#..#.[.]
                pos = 6
                if map[i + 1][pos] == "#":
                    trees = trees + 1
                continue
            elif pos+2 == len(map[i]):  #..#..#[.].
                pos = 5
                if map[i + 1][pos] == "#":
                    trees = trees + 1
                continue
            elif pos+3 == len(map[i]):  #..#..[#]..
                pos = 4
                if map[i + 1][pos] == "#":
                    trees = trees + 1
                continue
            elif pos+4 == len(map[i]):  #..#.[.]#..
                pos = 3
                if map[i + 1][pos] == "#":
                    trees = trees + 1
                continue
            elif pos+5 == len(map[i]):  #..#[.].#..
                pos = 2
                if map[i + 1][pos] == "#":
                    trees = trees + 1
                continue
            elif pos+6 == len(map[i]):  #..[#]..#..
                pos = 1
                if map[i + 1][pos] == "#":
                    trees = trees + 1
                continue
            elif pos+7 == len(map[i]):  #.[.]#..#..
                pos = 0
                if map[i + 1][pos] == "#":
                    trees = trees + 1
                continue
            else:
                if map[i+1][pos+7] == "#":
                    trees = trees+1
            pos = pos+7


def solve_problem_2_4(map):
    trees = 0
    pos = 0
    for i in range(len(map)):
        if i != 0:
            i = a+2
        if i+3 > len(map):
            return trees
        else:
            if pos+1 == len(map[i]):  #..#..#.[.]
                pos = 0
                if map[i+2][pos] == "#":
                    trees = trees + 1
                continue
            else:
                if map[i+2][pos+1] == "#":
                    trees = trees+1
            pos = pos+1
            a = i


print(37 * solve_problem_2_3(read_input()) * solve_problem_2_2(read_input()) * solve_problem_2_1(read_input()) * solve_problem_1(read_input()))

#print(solve_problem_2_4(read_input()))