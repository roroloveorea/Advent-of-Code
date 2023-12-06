
with open('Day 5/input.txt', 'r') as file:
    myDict = {}

    for line in file:
        line = line.strip()
        print(line)

        if line.startswith('seeds:'):
            current_map = "seed"
            myDict[current_map] = list(map(int, line.split()[1:]))
        elif line.startswith('seed-to-soil map:'):
            current_map = "seed_to_soil_map"
        elif line.startswith('soil-to-fertilizer map:'):
            current_map = "soil_to_fertilizer_map"
        elif line.startswith('fertilizer-to-water map:'):
            current_map = "fertilizer_to_water_map"
        elif line.startswith('water-to-light map:'):
            current_map = "water_to_light_map"
        elif line.startswith('light-to-temperature map:'):
            current_map = "light_to_temperature_map"
        elif line.startswith('temperature-to-humidity map:'):
            current_map = "temperature_to_humidity_map"
        elif line.startswith('humidity-to-location map:'):
            current_map = "humidity_to_location_map"
        else:
            
            numbers_list = list(map(int, line.split()))
            if numbers_list == []:
                continue
            if current_map not in myDict:
                myDict[current_map] = [numbers_list]
            else:
                
                # print(current_map)
                myDict[current_map].append(numbers_list)



words = ["seed","soil","fertilizer","water","light", "temperature","humidity","location"]

for word in range(len(words)):
    current_word = words[word]
    next_word = words[word+1]
    current_map = f'{current_word}_to_{next_word}_map'
    for conditions in myDict[current_word]:
        flag = False
        print(f"looking for {current_word}: {conditions} ")
        for next_item in myDict[current_map]:
            
            # print(f"{next_word}: {next_item}")
            if conditions in range(next_item[1],next_item[1]+next_item[2]):
                flag = True
                the_jump = conditions - next_item[1]
                # print(the_jump)
                
                next_source = next_item[0]+the_jump 
                if next_word not in myDict:
                    myDict[next_word] = [next_source]
                else:
                    
                    # print(current_map)
                    # print(myDict[next_word])
                    myDict[next_word].append(next_source)
        if flag == False:
            if next_word not in myDict:
                    myDict[next_word] = [conditions]
            else:
                    
                    print(f"not found, so adding to {next_word}: {conditions}")
                    print(myDict[next_word])
                    myDict[next_word].append(conditions)
                    
            
            
    print(f"{next_word}: {myDict[next_word]}") 
    if next_word == "location":
        print(min(myDict[next_word]))
        break
                    