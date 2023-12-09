import math
with open('Day 8/input.txt', 'r') as file:  
    network = {}
    end_with_A = []
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
            if key.endswith("A"):
                end_with_A.append(key)
def find_LCM(lst):
    lcm = lst[0]
    for i in range(1,len(lst)):
        lcm = lcm*lst[i]//math.gcd(lcm,lst[i])
        
    return lcm           
print(network)
print(instructions)
len_of_instructions = len(instructions)
print('len of ins', len_of_instructions)
print(end_with_A)
# node = "AAA"

# counter = 0
# print(network[node])
number_counts = []
# print(len_of_instructions%1)
for node in end_with_A:
    i = 1
    counter = 0
    print(node)
    while node.endswith("Z") !=True:
        i = i%len_of_instructions
        # print(i)
        current_instruction = instructions[i-1]
        node = network[node][0] if current_instruction == "L" else network[node][1]
        print(node)
        i+=1
        # print("i is now", i)
        counter+=1
        # if counter == 3:
        #     break
        
    number_counts.append(counter)
        
print(number_counts)

print(find_LCM(number_counts))

    