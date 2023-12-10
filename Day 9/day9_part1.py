def check_zero(lst):
    for item in lst:
        if item !=0:
            return False
    return True
with open('Day 9/input.txt', 'r') as file: 
    ans_list = []
    sum_num=0
    for line in file:
        list_of_number = []
        data = line.split()
        data = list(map(int, data))
        list_of_number.append(data)
        print(list_of_number)
        while check_zero(list_of_number[-1])==False:
            list_of_diff = []
            for i in range(len(list_of_number[-1])-1):
                number_diff = list_of_number[-1][i+1] - list_of_number[-1][i]
                list_of_diff.append(number_diff)
            if len(list_of_diff) == 0:
                break
            list_of_number.append(list_of_diff)
        print(list_of_number)
        # list found, do extrapolation now
        new_number = 0
        # for j in list_of_number[-1::-1]:
        #     # print(j)
        #     new_number += j[-1]
        #     print(new_number)
        #     # list_of_number[j-1].append(new_number)
        for j in list_of_number[-1::-1]:
            # print(j)
            new_number = j[0] - new_number
            print(new_number)
            # list_of_number[j-1].append(new_number)
            
        sum_num+=new_number
        
    print(sum_num)
            
            
        
                
        