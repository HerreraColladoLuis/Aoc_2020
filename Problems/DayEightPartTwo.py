def to_list_program():
    input = open("C:\\AdventOfCode\\DayEight\\DayEightInput.txt", "r")
    return input.readlines()


def solve_program(program_list):
    accumulator = 0
    instr_list = []
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


def fix_program(program_list, program_list_mod, i):
    if program_list[i].split(" ")[0] != "acc":
        if program_list[i].split(" ")[0] == "nop":
            new_instr = "jmp " + program_list[i].split(" ")[1]
        else:
            new_instr = "nop " + program_list[i].split(" ")[1]
        program_list_mod[i] = new_instr
        result = solve_program(program_list_mod)
        if result[1]:
            return result[0]
        else:
            program_list_mod[i] = program_list[i]

    return fix_program(program_list, program_list_mod, i+1)


print(fix_program(to_list_program(), to_list_program(), 0))
