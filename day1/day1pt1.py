file_path = 'calibrations.txt'
calibration_sum = 0

int_dict = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '0': 0
}

with open(file_path, 'r') as file:
    # go through each line of file
    digit_one = None
    digit_two = None

    for line in file:
        # find first digit
        for ch in line:
            if ch in int_dict:
                digit_one = int_dict[ch]
                break
        # find second digit
        for ch in reversed(line):
            if ch in int_dict:
                digit_two = int_dict[ch]
                break
        calibration = digit_one * 10 + digit_two
        calibration_sum += calibration
print(calibration_sum)