def is_gear(ch):
    if ch == "*":
        return True
    return False

# returns all (row, col) of gears at this number
def find_gears(row, col, schematic_matrix):
    gears = set()

    num_rows = len(schematic_matrix)
    # left neighbor
    if (col - 1) >= 0:
        left_neighbor = schematic_matrix[row][col-1]
        if is_gear(left_neighbor):
            gears.add((row, col-1))
    # right neighbor
    num_cols = len(schematic_matrix[row])
    if (col + 1) < num_cols:
        right_neighbor = schematic_matrix[row][col+1]
        if is_gear(right_neighbor):
            gears.add((row, col+1))

    # top neighbor
    if (row - 1) >= 0:
        top_neighbor = schematic_matrix[row-1][col]
        if is_gear(top_neighbor):
            gears.add((row-1, col))
    # bottom neighbor
    if (row + 1) < num_rows:
        bottom_neighbor = schematic_matrix[row+1][col]
        if is_gear(bottom_neighbor):
            gears.add((row+1, col))

    # top-left neighbor
    if ((row - 1) >= 0) and ((col - 1) >= 0):
        top_left = schematic_matrix[row-1][col-1]
        if is_gear(top_left):
            gears.add((row-1, col-1))
    # top-right neighbor
    if ((row - 1) >= 0) and ((col+1) < len(schematic_matrix[row-1])):
        top_right = schematic_matrix[row-1][col+1]
        if is_gear(top_right):
            gears.add((row-1, col+1))
    # bottom-left neighbor
    if ((row+1) < num_rows) and ((col - 1) >= 0):
        bottom_left = schematic_matrix[row+1][col-1]
        if is_gear(bottom_left):
            gears.add((row+1, col-1))
    # bottom-right neighbor
    if ((row+1) < num_rows) and ((col+1) < len(schematic_matrix[row+1])):
        bottom_right = schematic_matrix[row+1][col+1]
        if is_gear(bottom_right):
            gears.add((row+1, col+1))
    # if none are true, return False
    return gears

# read in file input as matrix
res = 0
file_path = "engine_schematic.txt"
schematic_matrix = []
with open(file_path, 'r') as file:
    for line in file:
        row = list(line.strip()) # remove new line characters
        schematic_matrix.append(row)

# gears dict, key is (row, col) of gear & val is a list of numbers at the gear
gears_dict = {}

# go through each row of the matrix
for i, row in enumerate(schematic_matrix):
    # iterate through row to find the start of a number
    j = 0
    while j < len(row):
        val = row[j]

        # if True, found the start of a number
        if val.isdigit():
            number = val
            gears = set()
            # find gears at this number
            gears |= find_gears(i, j, schematic_matrix)
            j += 1

            while(j < len(row) and row[j].isdigit()):
                number = number + row[j]
                gears |= find_gears(i, j, schematic_matrix)
                j += 1

            # for each gear, add to dict: (row, col) of gear as key, number as value
            for gear in gears:
                if gear in gears_dict:
                    gears_dict[gear].append(int(number))
                else:
                    gears_dict[gear] = [int(number)]
        else:
            j += 1

# iterate through dict and calculate powers
for numbers_list in gears_dict.values():
    if len(numbers_list) == 2:
        power = numbers_list[0] * numbers_list[1]
        res += power
# print final result
print(res)