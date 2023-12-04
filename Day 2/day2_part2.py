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
    max_red=0
    max_blue=0
    max_green=0
    
    
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
                if number > max_red:
                    max_red = number 
                    
            elif color == 'blue':
                if number > max_blue:
                    max_blue = number 
            else:
                if number > max_green:
                    max_green = number 
    product = max_red * max_blue * max_green
    sum+=product
    
print(sum)

                
        