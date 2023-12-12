# Advent of Code - Day 02 - Cube Conundrum | filename: day_02_cube_conundrum.py
# required libraries
import re

# import the txt file and reads each line into a list of strings
file = open('day_02_input.txt', 'r')
lines = file.read().splitlines()

# my functions
def get_info(str_arg, req):  # split the color and count given group
    if req == 'num': return int(re.split(' ', str_arg)[0])
    elif req == 'color': return re.split(' ', str_arg)[1]

def find_true(boolean_list): # given list of [True, False, True, True...], return True indexes
    return [index for index, value in enumerate(boolean_list) if value]

# game limitations:
game_limits = [['red', 12], ['green', 13], ['blue', 14]]  # can add or remove limits
game_possibility = []
games_power = [] # ADDED FOR PART 2

for i in range(len(lines)):
    # parse each string to get data out
    separated = re.split('; |: ', lines[i])  # split at ":" after game number and ";" between sets
    current_game = [re.split(', ', separated[j]) for j in range(len(separated))]
    max_green, max_red, max_blue = 0, 0, 0     # ADDED FOR PART 2:
    set_possibility = []
    for set in current_game[1:]:  # for each set of cubes revealed from the bag
        color_possibility = []
        for index, string in enumerate(set):
            color = get_info(string, 'color')
            quantity = get_info(string, 'num')
            # is the color acceptable?
            if any(color in sublist for sublist in game_limits):

                # ADDED FOR PART 2: get max quantity that's pulled from the bag for each color
                if color == 'green' and quantity > max_green:
                    max_green = quantity
                elif color == 'red' and quantity > max_red:
                    max_red = quantity
                elif color == 'blue' and quantity > max_blue:
                    max_blue = quantity

                # check quantity against the relevant rule in game_limits
                rule = next(i for i, j in enumerate(game_limits) if color in j)
                if quantity <= (game_limits[rule][1]):
                    color_possibility.append(True)
                else:
                    color_possibility.append(False)
            else:
                color_possibility.append(False)

        if all(color_possibility): # if all colors and quantities are ok, set is possible
            set_possibility.append(True)
        else:
            set_possibility.append(False)

    if all(set_possibility): # if all sets are possible, game is possible
        game_possibility.append(True)
    else:
        game_possibility.append(False)

    # ADDED FOR PART 2:
    power = max_green * max_blue * max_red
    games_power.append(power)

# get indexes of true games, then add 1 to get game number
indexes = find_true(game_possibility)
game_numbers = [x + 1 for x in indexes]
answer = sum(game_numbers)
print('Part 1 answer = ' + str(answer))

# PART 2
sum_of_powers = sum(games_power)
print('Part 2 answer = ' + str(sum_of_powers))