with open('Day 13/input.txt', 'r') as file:
    ash_n_rocks = []
    lst = []
    for line in file:
        line = line.replace("\n","")


        if line == '':
            ash_n_rocks.append(lst.copy())  # Use lst.copy() to create a new list
            lst.clear()
            continue
        lst.append(line)
        # print(lst)

    # Append the last pattern if the file doesn't end with an empty line
    if lst:
        ash_n_rocks.append(lst.copy())



def rotate_matrix(matrix):
    
    return [''.join(row[i] for row in matrix) for i in range(len(matrix[0]))]

def check_reflection(matrix, row):
    for front, back in zip(matrix[row-1::-1], matrix[row:]):
        # print(f"front {front}")
        # print(f"back {back}")
        if front != back:
            # print("dun match")
            return False
    return True
def check_reflection2(matrix, row):
    count=0
    for front, back in zip(matrix[row-1::-1], matrix[row:]):
        # print(f"front {front}")
        # print(f"back {back}")
        if front != back:
            # print("dun match")
            for i,j in zip(front,back):
                if i != j:
                    count+=1
    if count!=1: return False 
    else: return True

#find horizontal first
def part1(ash_n_rocks):
    row_num = col_num = 0
    for pattern in ash_n_rocks:
        found_row = False
        for row in range(1,len(pattern)):
            if check_reflection(pattern,row):
                found_row = True
                row_num+=row
                break

                    
        if found_row==False:
            #do col now
            transpose=rotate_matrix(pattern)
            for row in range(1,len(transpose)):
                if check_reflection(transpose,row):
                    col_num+=row
                    break
                
    print(f"part 1: {col_num + (row_num*100)}")
    
def part2(ash_n_rocks):
    row_num = col_num = 0
    for pattern in ash_n_rocks:
        found_row = False
        for row in range(1,len(pattern)):
            if check_reflection2(pattern,row):
                found_row = True
                row_num+=row
                break

                    
        if found_row==False:
            #do col now
            transpose=rotate_matrix(pattern)
            for row in range(1,len(transpose)):
                if check_reflection2(transpose,row):
                    col_num+=row
                    break
                
    print(f"part 2: {col_num + (row_num*100)}")
    

part1(ash_n_rocks)
part2(ash_n_rocks)

