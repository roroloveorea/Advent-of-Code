with open('Day 4/input.txt', 'r') as f:
    # Iterate through each line
    matrix = []
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
sum = 0
for card in matrix:
    count = 0
    for i in range(len(card[0])):
        win_num = card[0][i]
        for j in range(len(card[1])):
            # print(card[1][j])
            if card[1][j] == win_num:
                
                count+=1
                # print("count", count)
    print(count)
    print(multiply(count))
    sum+=multiply(count)
    
print(sum)