file_path = 'calibrations.txt'
calibration_sum = 0

num_dict = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

with open(file_path, 'r') as file:
    # go through each line of file
    for line in file:
        digit_one = None
        digit_two = None
        found = False
        # find first digit
        for i in range(len(line)):
            for j in range(i, i+5):
                if j < len(line):
                    subspan = line[i:j+1]
                    if subspan in num_dict:
                        digit_one = num_dict[subspan]
                        found = True
            if found == True:
                break
        found = False
        # find second digit
        for j in range(len(line) - 1, -1, -1):
            for i in range(j, j-5, -1):
                if i >= 0:
                    subspan = line[i:j+1]
                    if subspan in num_dict:
                        digit_two = num_dict[subspan]
                        found = True
            if found == True:
                break
        calibration = digit_one * 10 + digit_two
        calibration_sum += calibration

print(calibration_sum)