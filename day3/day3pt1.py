def is_symbol(ch):
    if ch == "." or ch.isdigit():
        return False
    return True

# returns True if at least one neighbor is a symbol
def is_part_num(row, col, schematic_matrix):
    num_rows = len(schematic_matrix)
    # left neighbor
    if (col - 1) >= 0:
        left_neighbor = schematic_matrix[row][col-1]
        if is_symbol(left_neighbor):
            return True
    # right neighbor
    num_cols = len(schematic_matrix[row])
    if (col + 1) < num_cols:
        right_neighbor = schematic_matrix[row][col+1]
        if is_symbol(right_neighbor):
            return True

    # top neighbor
    if (row - 1) >= 0:
        top_neighbor = schematic_matrix[row-1][col]
        if is_symbol(top_neighbor):
            return True
    # bottom neighbor
    if (row + 1) < num_rows:
        bottom_neighbor = schematic_matrix[row+1][col]
        if is_symbol(bottom_neighbor):
            return True

    # top-left neighbor
    if ((row - 1) >= 0) and ((col - 1) >= 0):
        top_left = schematic_matrix[row-1][col-1]
        if is_symbol(top_left):
            return True
    # top-right neighbor
    if ((row - 1) >= 0) and ((col+1) < len(schematic_matrix[row-1])):
        top_right = schematic_matrix[row-1][col+1]
        if is_symbol(top_right):
            return True
    # bottom-left neighbor
    if ((row+1) < num_rows) and ((col - 1) >= 0):
        bottom_left = schematic_matrix[row+1][col-1]
        if is_symbol(bottom_left):
            return True
    # bottom-right neighbor
    if ((row+1) < num_rows) and ((col+1) < len(schematic_matrix[row+1])):
        bottom_right = schematic_matrix[row+1][col+1]
        if is_symbol(bottom_right):
            return True
    # if none are true, return False
    return False


# read in file input as matrix
res = 0
file_path = "engine_schematic.txt"
schematic_matrix = []
with open(file_path, 'r') as file:
    for line in file:
        row = list(line.strip()) # remove new line characters
        schematic_matrix.append(row)

# go through each row of the matrix
for i, row in enumerate(schematic_matrix):
    # iterate through row to find the start of a number
    j = 0
    while j < len(row):
        val = row[j]

        # if True, found the start of a number
        if val.isdigit():
            part_num = False
            number = val
            # go through all neighbors and see if is symbol
            if is_part_num(i, j, schematic_matrix):
                part_num = True
            j += 1

            while(j < len(row) and row[j].isdigit()):
                number = number + row[j]
                # if part_num is still False, see if should be true now
                if not part_num and is_part_num(i, j, schematic_matrix):
                    part_num = True
                j += 1

            # at the end of the cur number,, if is_part_num True, add to res
            if part_num:
                res += int(number)
        else:
            j += 1

# print final result
print(res)






