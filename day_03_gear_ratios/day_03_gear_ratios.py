# Advent of Code - Day 03 - Gear Ratios
# filename: day_03_gear_ratios.py | 11 Dec 2023

# necessary imports
import re

# import the txt file and reads each line into a list of strings
file = open('day_03_input.txt', 'r')
lines = file.read().splitlines()

# region PART 1

def box_builder(row_number, index_start, index_end):
    # helper function that takes a row number and a pair of indexes (number start and number end)
    # and builds a box around it for checking for symbols
    row_above = []; row_below = []; same_row = []
    if index_start == 0: # skip "left check" for first column:
        for i in range(index_end - index_start + 1):
            row_above.append((row_number - 1, i + index_start + 1))
            same_row = [(row_number, index_end)]
            row_below.append((row_number + 1, i + index_start + 1))
    elif index_end == len(lines[row_number]): # skip "right check" for last column:
        for i in range(index_end - index_start + 1):
            row_above.append((row_number - 1, i + index_start - 1))
            same_row = [(row_number, index_start -1), (row_number, index_end - 1)]
            row_below.append((row_number + 1, i + index_start - 1))
    else:
        for i in range(index_end - index_start + 2):
            row_above.append((row_number - 1, i + index_start - 1))
            same_row = [(row_number, index_start -1), (row_number, index_end)]
            row_below.append((row_number + 1, i + index_start - 1))
    return row_above, same_row, row_below

part_numbers = [] # list of numbers that are adjacent to symbols

for i in range(len(lines)):
    numbers = re.findall(r'\d+', lines[i]) # find all numbers
    indexes = [(m.start(0), m.end(0)) for m in re.finditer(r'\d+', lines[i])]  # grab their indexes

    for j in range(len(indexes)): # per number
        check_top = False; check_mid = False; check_bot = False

        a, b, c = box_builder(i, indexes[j][0], indexes[j][1])
        if i > 0: # skip "row above" check for first row
            for k in range(len(a)):
                current_character = lines[a[k][0]][a[k][1]]
                if not any([current_character.isalnum(), current_character == "."]): # ignore alphanumeric and "."
                    check_top = True
        else: check_top = False

        for m in range(len(b)): # current row
            current_character = lines[b[m][0]][b[m][1]]
            if not any([current_character.isalnum(), current_character == "."]): # ignore alphanumeric and "."
                check_mid = True

        if i < len(lines) - 1: # skip "row below" check for last row
            for n in range(len(c)):
                current_character = lines[c[n][0]][c[n][1]]
                if not any([current_character.isalnum(), current_character == "."]): # ignore alphanumeric and "."
                    check_mid = True
        else: check_bot = False

        # if you found a symbol anywhere around the number, it's a valid part number
        if check_top == True or check_mid == True or check_bot == True:
            part_numbers.append(numbers[j])

part_nums_to_int = list(map(int, part_numbers)) # from list of strings to list of integers
answer = sum(part_nums_to_int)
print("Part 1 answer = " + str(answer))
# endregion

# region PART 2
gear_ratios = []
gears = []

for i in range(len(lines)): # per line
    stars = re.findall(r'[*]', lines[i]) # find all asterix
    star_indexes = [(m.start(0), m.end(0)) for m in re.finditer(r'[*]', lines[i])] # get their indexes

    for j in range(len(star_indexes)): # per asterix
        a, b, c = box_builder(i, star_indexes[j][0], star_indexes[j][1])
        all_part_numbers = []
        if i > 0:  # skip "row above" check for first row
            for k in range(len(a)):
                current_character = lines[a[k][0]][a[k][1]]
                if current_character.isdigit():
                    top_row = lines[a[k][0]]
                    top_right_dot = top_row.find(".", a[k][1], len(top_row))
                    top_left_dot = top_row.rfind(".", 0, a[k][1]+1)
                    numero_top = top_row[top_left_dot + 1:top_right_dot]
                    if numero_top not in all_part_numbers:
                        all_part_numbers.append(numero_top)
        else:
            continue

        for m in range(len(b)):  # current row
            current_character = lines[b[m][0]][b[m][1]]
            if current_character.isdigit():  # look for numbers
                current_row = lines[b[m][0]]
                if lines[b[m][0]][b[m][1]+1] == "*":
                    mid_left_dot = current_row.rfind(".", 0, b[m][1])
                    numero_mid = current_row[mid_left_dot + 1 :b[m][1] + 1]
                    if numero_mid not in all_part_numbers:
                        all_part_numbers.append(numero_mid)
                elif lines[b[m][0]][b[m][1]-1] == "*":
                    mid_right_dot = current_row.find(".", b[m][1], len(current_row))
                    numero_mid = current_row[b[m][1]:mid_right_dot]
                    if numero_mid not in all_part_numbers:
                        all_part_numbers.append(numero_mid)

        if i < len(lines) - 1:  # skip "row below" check for last row
            for n in range(len(c)):
                current_character = lines[c[n][0]][c[n][1]]
                if current_character.isdigit():
                    bot_row = lines[c[n][0]]
                    bot_right_dot = bot_row.find(".", c[n][1], len(bot_row))
                    bot_left_dot = bot_row.rfind(".", 0, c[n][1])
                    numero_bot = bot_row[bot_left_dot + 1:bot_right_dot]
                    if numero_bot not in all_part_numbers:
                        all_part_numbers.append(numero_bot)
        else:
            continue

        if len(all_part_numbers) == 2:
            gears.append(all_part_numbers)
            gear_ratios.append(int(all_part_numbers[0]) * int(all_part_numbers[1]))

print(gears)
print(gear_ratios)
answer2 = sum(gear_ratios)
print("Part 2 answer = " + str(answer2))
# endregion