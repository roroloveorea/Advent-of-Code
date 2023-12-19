def rotate_matrix(matrix):
    
    return [''.join(row[i] for row in matrix) for i in range(len(matrix[0]))]
def count_rocks(lst):
    count=0
    for i in range(len(lst)):
        if lst[i] == "O":
            count+=1
    return count
def shift_rocks(list_of_rocks):
    list_of_cube = []
    string1 = ''
    for rocks in range(len(list_of_rocks)):
        if list_of_rocks[rocks] == "#":
            list_of_cube.append(rocks)
    print(list_of_cube)
    for i in range(len(list_of_cube)):
        
        if i == 0:

            num_of_rocks = count_rocks(list_of_rocks[:list_of_cube[i]])
            print(num_of_rocks)
            for j in range(num_of_rocks):
                string1+='O'
            for j in range(len(string1),list_of_cube[i]):
                string1+='.'
            string1+="#"
        else:
            num_of_rocks = count_rocks(list_of_rocks[list_of_cube[i-1]:list_of_cube[i]])
            for j in range(num_of_rocks):
                string1+='O'
            for j in range(len(string1),list_of_cube[i]):
                string1+='.'
            string1+="#"
   
    if(len(list_of_cube)!=0):       
        last_num_of_rocks = count_rocks(list_of_rocks[list_of_cube[-1]:])
        for i in range(last_num_of_rocks):
            string1+="O"
        for i in range(len(string1),len(list_of_rocks)):
            string1+="."
    else:
        num_of_rocks = count_rocks(list_of_rocks)
        for j in range(num_of_rocks):
                string1+='O'
        for j in range(len(string1),len(list_of_rocks)):
            string1+='.'
            
    print(string1)
    return string1
    

            
            
            
            
        

with open('Day 14/input.txt', 'r') as file:
    platform = []

    for line in file:
        line = line.replace("\n","")
        platform.append(line)  # Use lst.copy() to create a new list
    platform = rotate_matrix(platform)
    
print(platform)
for i in platform:
    print(i)
new_platform = []
for loads in platform:
    new_string = shift_rocks(loads)
        
    new_platform.append(new_string)
    
print(new_platform)
the_sum=0
for rows in new_platform:
    for i in range(len(rows)):
        if rows[i] =="O":
            print("the O is equal", len(rows)-i)
            the_sum+=(len(rows)-i)
            
print(the_sum)
        
                
            
            
        
# new_platform = rotate_matrix(platform)
# print(new_platform)
    
