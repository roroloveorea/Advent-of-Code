with open('Day 8/input.txt', 'r') as file:  
    network = {}
    content = file.read()
    lines = content.split('\n')
    # Extract the first row as a list
    instructions = list(lines[0])
    for line in lines[2:]:
        if line:
            key, value = line.split('=')
            key = key.strip()
            value = value.replace("(","")
            value = list(map(str.strip, value.strip(")").split(',')))
            network[key] = value
            
print(network)
print(instructions)
len_of_instructions = len(instructions)
print('len of ins', len_of_instructions)
node = "AAA"
i = 1
counter = 0
print(network[node])
# print(len_of_instructions%1)
while node != "ZZZ":
    i = i%len_of_instructions
    print(i)
    current_instruction = instructions[i-1]
    node = network[node][0] if current_instruction == "L" else network[node][1]
    print(node)
    i+=1
    print("i is now", i)
    counter+=1
    # if counter == 3:
    #     break
    
print(counter)
    