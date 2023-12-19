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
            
    for i in range(list_of_cube[-1]+1,len(list_of_rocks)):
        string1+="."
            
    print(string1)
    
