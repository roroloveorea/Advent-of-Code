import math
def find_distance(duration):
    list_of_distance = []
    for i in range(0,duration+1):
        # if i == duration:
        #     list_of_distance.append(0)
        # else:
        distance = (i)*(duration-i)
        list_of_distance.append(distance)
        
    return list_of_distance
def find_range(duration,distance):
    hold1 =  int((((duration/2)**2)-distance)**0.5 + duration/2)
    hold2 = int(duration/2 - (((duration/2)**2)-distance)**0.5)
    print(hold1,hold2)
    
    number = max(hold1,hold2) - min(hold1,hold2)
    return number

print(find_distance(5))             
with open('Day 6/input.txt', 'r') as file:    
    # print(file)
    myList = []
    for line in file:
        print(line)
        data = line.split(":")[1:][0].replace(" ", "")
        data = data.replace("\n", "")
        myList.append(data)
    print(myList)

ans = find_range(int(myList[0]),int(myList[1]))

# for timing in range(len(myList[0])):
#     time = int(myList[0][timing])
#     # print(time)
#     # durations = find_distance(time)
#     # distance = int(myList[1][timing])
#     # print(distance)
#     # output = sum(i > distance for i in durations)
#     # print(output)
#     output = find_range(int(myList[0][timing]),int(myList[1][timing]))
#     ans*=output
print(ans)

# find_range(5,4)
# print(find_range(5,4))

                                                                                                                                  