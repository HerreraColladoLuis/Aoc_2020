import re

def read_input():
    input = open("C:\\AdventOfCode\\DayFour\\DayFourInput.txt", "r")
    list = []
    passport = ""
    for line in input.readlines():
        if line == '\n':
            list.append(passport)
            passport = ""
            continue
        if passport == "":
            passport = passport + line[:-1]
        else:
            passport = passport + " " + line[:-1]
    list.append(passport)
    return list


def solve_problem(list):
    valid_count = 0
    for passport in list:
        if is_valid(passport):
            valid_count = valid_count+1

    return valid_count


def is_valid(passport):
    keys_list = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    passport_list = passport.split(" ")
    counter = 0
    for dupla in passport_list:
        key = dupla.split(":")[0]
        value = dupla.split(":")[1]
        if key in keys_list:
            keys_list.remove(key)

            if key == "byr":
                if re.match('[0-9]{4}$', value):
                    if 1919 < int(value) < 2003:
                        counter=counter+1

            elif key == "iyr":
                if re.match('[0-9]{4}$', value):
                    if 2009 < int(value) < 2021:
                        counter=counter+1

            elif key == "eyr":
                if re.match('[0-9]{4}$', value):
                    if 2019 < int(value) < 2031:
                        counter=counter+1

            elif key == "hgt":
                if re.match('[0-9]{2}[a-z]{2}$', value) or re.match('[0-9]{3}[a-z]{2}', value):
                    if value[-2:] == "cm":
                        num = value.split('c')[0]
                        if 149 < int(num) < 194:
                            counter=counter+1
                    elif value[-2:] == "in":
                        num = value.split('i')[0]
                        if 58 < int(num) < 77:
                            counter=counter+1

            elif key == "hcl":
                if re.match('#[a-f0-9]{6}$', value):
                    counter=counter+1

            elif key == "ecl":
                if value in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
                    counter=counter+1

            elif key == "pid":
                if re.match('[0-9]{9}$', value):
                    counter=counter+1

    if counter == 7:
        return True
    else:
        return False


print(solve_problem(read_input()))