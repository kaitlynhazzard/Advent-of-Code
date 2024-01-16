file_path = "almanac.txt"

with open(file_path, 'r') as file:
    lines = file.readlines()
    num_of_lines = len(lines)

    # curr will first represent seeds, then update to soil, then furtilizer, etc
    curr = lines[0].split(':')[1].split() # get list of all seeds

    # lower bound input, upper bound input, output start 
    # for current mapping: seed_to_soil / soil_to_furtilizer etc
    curr_mapping = {} 
    
    for i in range(2, num_of_lines):
        line = lines[i]

        # skip over header lines
        if "map" in line:
            continue
        
        # update curr_mapping once you get to newline
        if line == '\n':
            # iterate over each val in curr to update
            for idx, val in enumerate(curr):
                # see if the val corresponds with a range in curr_mapping
                for key, output_start in curr_mapping.items():
                    lower_bound, upper_bound = key
                    if int(val) >= lower_bound and int(val) <= upper_bound:
                        curr[idx] = output_start + (int(val) - lower_bound)
                        break # found the mapping for this val
                # if no input output mapping, keep the current ouptut

            curr_mapping = {} # clear the mapping so that it can be reused for next mapping
            continue
        
        # if line not a header or newline, it's a mapping; add line to curr_mapping
        destination, source, mapping_range = line.split()
        lower_bound_input = int(source)
        upper_bound_input = int(source) + int(mapping_range) - 1
        curr_mapping[(lower_bound_input, upper_bound_input)] = int(destination)

# final curr_mapping update
for idx, val in enumerate(curr):
    for key, output_start in curr_mapping.items():
        lower_bound, upper_bound = key
        if int(val) >= lower_bound and int(val) <= upper_bound:
            curr[idx] = output_start + (int(val) - lower_bound)
            break

print(min(curr))