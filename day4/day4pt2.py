def format_numbers(nums):
    # account for case where there are two spaces between 
    # numbers before splitting by whitespace
    nums = nums.replace('  ', ' ')
    return nums.split()

file_path = 'scratchcards.txt'
tot_num_cards = 0

# key: the card number, value: number of copies of this card number
copies_of_card = {}

with open(file_path, 'r') as file:
    lines = file.readlines()
    num_of_cards = len(lines)
    for card_number in range(1, num_of_cards + 1):
        copies_of_card[card_number] = 1

    # go through each card
    for line in lines:
        # get id of current card
        info = line.split(':')
        card_num = int(info[0].split()[1])

        # find number of matches
        winning_nums, your_nums = info[1].split('|')
        winning_nums = format_numbers(winning_nums)
        your_nums = format_numbers(your_nums)
        # TODO: optimize
        matches = sum(num in winning_nums for num in your_nums)
        
        # find the cards you win a copy to
        for i in range(card_num+1, card_num+matches+1):
            # adjust the number of copies for the card won
            copies_of_card[i] = copies_of_card[i] + copies_of_card[card_num]

# sum of the number of copies for each card
print(sum(copies_of_card.values()))