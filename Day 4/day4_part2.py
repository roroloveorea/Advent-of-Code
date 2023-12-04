with open('Day 4/input.txt', 'r') as f:
    # Iterate through each line
    matrix = []
    card_instances = {}
    for line in f:
        # Split the line based on ':'
        card_number, card_data = map(str.strip, line.split(':'))

        # Split the card data into two lists separated by '|'
        left_list, right_list = map(str.split, card_data.split('|'))

        # Convert the lists to integers
        left_list = list(map(int, left_list))
        right_list = list(map(int, right_list))

        # Append the two lists to form a row in the matrix
        matrix.append([left_list, right_list])

def multiply(number):
    if number > 0:
        ans = 2**(number-1)
        return ans
    else:
        return 0
# print(matrix[0])
# sum = 0
for card in range(len(matrix)):
    card_instances[card]=card_instances.get(card, 0)+1
    win_number = set(matrix[card][0])
    my_numbers = set(matrix[card][1])
    wins = len(win_number.intersection(my_numbers))
    for free in range(1,wins+1):
        card_instances[card+free] = card_instances.get(card+free, 0) + card_instances.get(card, 0)
        
        
print(sum(card_instances.values()))
        
# print(sum+len(matrix)-1)