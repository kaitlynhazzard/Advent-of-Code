def format_numbers(nums):
    # account for case where there are two spaces between 
    # numbers before splitting by whitespace
    nums = nums.replace('  ', ' ')
    return nums.split()

file_path = 'scratchcards.txt'
sum_points = 0

with open(file_path, 'r') as file:
    # iterate over each card
    for line in file:
        card_points = 0
        winning_nums, your_nums = line.split(':')[1].split('|')

        # turn winning numbers and your numbers into list
        winning_nums = format_numbers(winning_nums)
        your_nums = format_numbers(your_nums)
        
        # go through each number in your_nums to calculate points for the card
        for num in your_nums:
            if num in winning_nums:
                card_points = card_points * 2 if card_points > 0 else 1
        sum_points += card_points

print(sum_points)
