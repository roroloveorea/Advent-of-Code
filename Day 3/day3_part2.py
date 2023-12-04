with open('Day3/input.txt', 'r') as f:
    myList = [line.strip() for line in f]
symbol_list = ['.','0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def append_gear(key, value):
    myDict.setdefault(key,[]).append(value)


# print(myList)
temp = []
array = []
myDict = {}
def check_if_valid(row,col_start,count,matrix):
    adjacent_positions = [
        (-1, -1), (-1, 0), (-1, 1),  # Top left, Top, Top right
        (0, -1),           (0, 1),   # Left,       , Right
        (1, -1),  (1, 0),  (1, 1)    # Bottom left, Bottom, Bottom right
    ]
    counter = 0
    for col in range(col_start,col_start+count):
        for dx, dy in adjacent_positions:
            new_row, new_col = row + dx, col + dy
            if new_row <0 or new_row>len(matrix)-1 or new_col<0 or new_col>len(matrix[row])-1:
                continue
            if matrix[new_row][new_col] == '*':
                append_gear((new_row,new_col),int(matrix[row][col_start:col_start+count]))
    
    
    

for stringNumber in range(len(myList)):
    i = 0
    stopper = 0
   
    print(myList[stringNumber])
    while i <len(myList[stringNumber]):
        # print("i is now", i)
        stopper +=1
        count = 1
        jump = 1
        flag = False
        if myList[stringNumber][i].isdigit():
            # print("symbol now",myList[stringNumber][i])
            for j in range(i+1,len(myList[stringNumber])):
                if myList[stringNumber][j].isdigit():
                    count+=1
                else:
                    break
            # print("count: ", count)
            print(myList[stringNumber][i:i+count])
            check_if_valid(stringNumber,i,count,myList)
                
                
                
            
        i+=count
        
def product(theset):
    answer = 1
    for i in theset:
        answer*=i   
    return int(answer) 

sum=0                
print(myDict) 
for item in myDict:
    print(set(myDict[item])) 
    theset = set(myDict[item])
    if len(theset) == 2:
        product1 = product(theset)
        print(product1)
        sum+=product1

print(sum)