# Advent of Code - Day 01 - Trebuchet
# filename: day_01_trebuchet.py | 04 Dec 2023

# region PART 1 Challenge:
# Given a list of strings that are a random mix of letters and numbers, get the first and
# last digit of each string, then return the sum of all the two-digit numbers

# import the txt file and reads each line into a list of strings
file = open('day_01_input.txt', 'r')
lines = file.read().splitlines()        # using readlines() puts \n at the end of each string

two_digit_lines = []                    # create parallel list of two digit integer output

for i in range(len(lines)):
    '''
    # solution 1: create a parallel list that says whether each char in the string is a digit
    digit_check = []
    
    for j in lines[0]:
        digit_check.append(j.isdigit())
    
    # return index for each pair of [index, value] in the digit_check if value = True
    locations = [k for k, x in enumerate(digit_check) if x]
    '''
    # solution 2: found a faster way, bypasses "digit_check" list containing booleans
    # return index for each pair of [index, value] if value of char is a digit
    locations = [k for k, x in enumerate(lines[i]) if x.isdigit()]

    first = lines[i][locations[0]]
    last = lines[i][locations[len(locations)-1]]

    two_digit_lines.append(int(first + last))
'''
# test result by writing to a new text file      ...        woooooooo! it works!
with open('testing.txt', 'w') as f:
    for line in two_digit_lines:
        f.write(str(line))              # needs to be a string to write
        f.write('\n')                   
'''
answer = sum(two_digit_lines)
# endregion

print("Part 1 answer = " + str(answer))


# region PART 2 Challenge:
# Repeat Part 1, except also consider any digits that are spelled out with letters.
# one, two, three, four, five, six, seven, eight, and nine also count as valid "digits"

# Game plan:
# do the integer check from Part 1 first, then do the word check and overwrite if smaller min
# or larger max is found

new_two_digit_lines = []                    # create parallel list of two digit integer output

for i in range(len(lines)):
    # integer check from Part 1:
    locations = [k for k, x in enumerate(lines[i]) if x.isdigit()]
    current_minimum = locations[0]
    current_maximum = locations[len(locations) - 1]

    first = lines[i][current_minimum]
    last = lines[i][current_maximum]

    #print('Part A first is ' + first)
    #print('Part A last is ' + last)

    # letters check for Part 2:
    # create array to keep track of occurrences of each word
    letter_numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    conversion = ['1','2','3','4','5','6','7','8','9']
    concat_lists = list(zip(letter_numbers, conversion))   # output is a list of tuples

    locations2 = []  # converting to flat list
    for n in range(len(letter_numbers)):
        as_flat = [item for item in concat_lists[n]]
        locations2.append(as_flat)
    #print(locations2)

    # find word numbers in the string and their locations
    for j in range(len(letter_numbers)):
        index = 0
        while index < len(lines[i]):
            index = lines[i].find(letter_numbers[j], index) # find occurrences, starting at index
            if index == -1: # if you don't find it, skip to the next word
                break
            locations2[j].append(index) #yes, it's supposed to be an int
            #print(str(letter_numbers[j]) + ' found at ' + str(index))
            index += len(letter_numbers[j]) # jump forward by amount = the length of the word
    #print(locations2)

    # check for lowest index
    for k in range(len(locations2)): # for each number
        if len(locations2[k]) > 1: # if any occurances of that number were found
            for m in range(2,len(locations2[k])): # check 3rd column and beyond for indexes
                if locations2[k][m] < current_minimum: # lower index than current minimum
                    first = locations2[k][1] # we have a new minimum, return the digit
                    current_minimum = locations2[k][m] # return the location

    # check for highest index
    for k in range(len(locations2)): # for each number
        if len(locations2[k]) > 1: # if any occurances of that number were found
            for m in range(2,len(locations2[k])): # check 3rd column and beyond for indexes
                if locations2[k][m] > current_maximum: # higher index than current maximum
                    last = locations2[k][1] # we have a new maximum, return the digit
                    current_maximum = locations2[k][m] # return the location

    #print('Part B first is ' + first)
    #print('Part B last is ' + last)

    new_two_digit_lines.append(int(first + last))
'''
# test result by writing to a new text file      ...        woooooooo! it works!
with open('testing2.txt', 'w') as f:
    for line in new_two_digit_lines:
        f.write(str(line))              # needs to be a string to write
        f.write('\n')
'''
answer2 = sum(new_two_digit_lines)
# endregion

print("Part 2 answer = " + str(answer2))