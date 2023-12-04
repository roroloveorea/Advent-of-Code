def read_games_from_file(file_path):
    games = []

    with open(file_path, 'r') as file:
        game_lines = file.readlines()

        for game_line in game_lines:
            game_data = game_line.strip().split(':')

            if len(game_data) == 2:
                game_number = game_data[0].strip()
                round_groups = [group.strip() for group in game_data[1].split(';')]

                game_dict = {'Game': game_number, 'Rounds': []}

                for round_group in round_groups:
                    color_data = round_group.split(',')
                    color_quantity = [item.strip() for item in color_data]
                    game_dict['Rounds'].append(color_quantity)

                games.append(game_dict)

    return games

myDict = read_games_from_file("Day 2/input.txt")

flag = False
sum = 0
for game in myDict:
    # print(game)
    game_number = game['Game']
    
    
    flag = True
    for round in game['Rounds']:
        if flag == False:
            break
        for ball in round:
            parts = ball.split()
            number = int(parts[0])
            color = parts[1]
            print(ball)
            if color == 'red':
                if number > 12:
                    flag = False
                    break
            elif color == 'blue':
                if number > 14:
                    flag = False
                    break
            else:
                if number > 13:
                    flag = False
                    break
    
    if flag == True:
        partA = game_number.split()
        sum += int(partA[1])
        print(game)
    
print(sum)
                
        