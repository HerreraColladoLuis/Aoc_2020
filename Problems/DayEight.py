def solve_program():
    input = open("C:\\AdventOfCode\\DayEight\\DayEightInput.txt", "r")
    accumulator = 0
    instr_list = []
    program_list = input.readlines()
    i = 0
    while i < len(program_list):
        if i in instr_list:
            return accumulator, False
        instr = program_list[i][:-1].split(" ")[0]
        action = program_list[i][:-1].split(" ")[1]
        if instr == 'acc':
            instr_list.append(i)
            if action[0] == '+':
                accumulator = accumulator + int(action.split('+')[1])
            else:
                accumulator = accumulator - int(action.split('-')[1])
            i = i + 1
        elif instr == 'jmp':
            instr_list.append(i)
            if action[0] == '+':
                i = i + int(action.split('+')[1])
            else:
                i = i - int(action.split('-')[1])
        else:
            instr_list.append(i)
            i = i + 1
    return accumulator, True


print(solve_program())
