file_path = 'data.txt'
sum_id_possible = 0

color_limits = {
    'red': 12,
    'green':  13,
    'blue': 14
}

with open(file_path, 'r') as file:
    # each game is on one line
    for line in file:
        impossible = False
        line_split = line.split(':')
        id = int(line_split[0][5:]) # game id

        # go through each subset of cubes to see if the game is impossible
        subsets = line_split[1].split(';')
        for subset in subsets:
            # separate by color (just green, just red, just blue)
            colors = subset.split(',')
            for color in colors:
                count_and_color = color.split()
                count = int(count_and_color[0])
                color = count_and_color[1]
                # if the count of a color > the color limit, game is invalid
                if count > color_limits[color]:
                    impossible = True
                    break
            if impossible == True:
                break
        # if game is possible, add the id to the sum
        if impossible == False:
            sum_id_possible += id

print(sum_id_possible)
    