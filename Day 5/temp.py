with open('Day 5/input.txt', 'r') as file:
    myDict = {}

    for line in file:
        line = line.strip()
        print(line)

        if line.startswith('seeds:'):
            current_map = "seed"
            numbers = line.split()[1:]
            seed_list = []
            for i in range(0, len(numbers), 2):
                seed_list.append([int(numbers[i]),int(numbers[i+1])])
            myDict[current_map] = seed_list
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
                
words = ['location', 'humidity', 'temperature', 'light', 'water', 'fertilizer', 'soil', 'seed']


for word in range(len(words)):
    not_found = True
    while not_found:
        current_word = words[word+1]
        next_word = words[word]
        current_map = f'{current_word}_to_{next_word}_map'
        for conditions in myDict[current_word]:
            
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
                    
# print(myDict)
# soils = []
# final_location = []
# print(len(myDict["seed"]))
# for seed in range(myDict["seeds"]):
#     print("looking for seed: ", seed)
#     for soil in myDict["seed_to_soil_map"]:
#         print("processing soil:" ,soil)
#         if seed in range(soil[1],soil[1]+soil[2]):
#             seed_to_soil_jump = seed - soil[1]
#             print(seed_to_soil_jump)
            
#             soil_source = soil[0]+seed_to_soil_jump
#             if "soils" not in myDict:
#                 myDict["soils"] = [soil_source]
#             else:
                
#                 # print(current_map)
#                 print(myDict["soils"])
#                 myDict["soils"].append(soil_source)
            
      
# print("soils: ", myDict["soils"])   
# for soil in myDict["soils"]:
#     print("looking for soils: ", soil)
#     for fertilizer in myDict["soil_to_fertilizer_map"]:
#         print("fertilizer:" ,fertilizer)
#         if soil in range(fertilizer[1],fertilizer[1]+fertilizer[2]):
#             soil_to_fertilizer_jump = soil - fertilizer[1]
#             print(soil_to_fertilizer_jump)
            
#             fertilizer_source = fertilizer[0]+soil_to_fertilizer_jump
#             if "fertilizer" not in myDict:
#                 myDict["fertilizer"] = [fertilizer_source]
#             else:
                
#                 # print(current_map)
#                 print(myDict["fertilizer"])
#                 myDict["fertilizer"].append(fertilizer_source)
# print("fertilizer: ", myDict["fertilizer"]) 

# for fertilizer in myDict["fertilizer"]:
#     print("looking for soils: ", fertilizer)
#     for water in myDict["fertilizer_to_water_map"]:
#         print("water:" ,water)
#         if fertilizer in range(water[1],water[1]+water[2]):
#             fertilizer_to_water_jump = fertilizer - water[1]
#             print(fertilizer_to_water_jump)
            
#             water_source = water[0]+fertilizer_to_water_jump 
#             if "water" not in myDict:
#                 myDict["water"] = [water_source]
#             else:
                
#                 # print(current_map)
#                 print(myDict["water"])
#                 myDict["water"].append(water_source)
# print("water: ", myDict["water"]) 