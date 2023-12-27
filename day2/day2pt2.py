file_path = 'data.txt'
sum_power = 0

with open(file_path, 'r') as file:
    # each game is on one line
    for line in file:
        # don't need id, only subsets
        subsets = line.split(':')[1].split(';')
        game_max_cubes = {
            'red': 0,
            'blue': 0,
            'green': 0
        }

        # go through each subset of cubes 
        for subset in subsets:
            colors = subset.split(',')
            # separate by color (just green, just red, just blue)
            for color in colors:
                count_and_color = color.split()
                count = int(count_and_color[0])
                color = count_and_color[1]
                # if the count of color for this subset is higher than
                # current max for the color, update dict
                if count > game_max_cubes[color]:
                    game_max_cubes[color] = count
        # calculate power for the game
        power = game_max_cubes['red'] * game_max_cubes['blue'] * game_max_cubes['green']
        sum_power += power

print(sum_power)