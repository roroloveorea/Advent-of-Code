with open('Day 11/input.txt', 'r') as file:
    universe = []
    for line in file:
        # line = line.split("\n")
        line = line.replace("\n","")
        
        universe.append(line)

def find_empty_row_col(universe):
    rows_no_galaxy = []
    have_galaxy_col = []
    for i in range(len(universe)):
        no_galaxy_row = True
        for j in range(len(universe[i])):
            if universe[i][j] == "#":
                have_galaxy_col.append(j)
                no_galaxy_row = False
        if no_galaxy_row:
            rows_no_galaxy.append(i)
            
    # print(rows_no_galaxy)
    have_galaxy_col = set(have_galaxy_col)
    col_no_galaxy = set(range(len(universe))) - have_galaxy_col
    col_no_galaxy = sorted(col_no_galaxy)
    # print(col_no_galaxy)
    return rows_no_galaxy, col_no_galaxy


rows_no_galaxy =[]
col_no_galaxy =[]
rows_no_galaxy, col_no_galaxy = find_empty_row_col(universe)  

def find_empty_galaxies(universe):
    galaxies = []
    for i in range(len(universe)):

        for j in range(len(universe[i])):
            if universe[i][j] == "#":
                galaxies.append([i,j])
                
    return galaxies

            
galaxies = find_empty_galaxies(universe)
total_distance = 0
aged_total_distance = 0
for source in range(len(galaxies)):
    # print(f"from source {galaxies[source]}")
    for dest in range(source+1,len(galaxies)):
        # print(f"to dest {galaxies[dest]}")
        num_row = 0
        for rows in rows_no_galaxy:
            # print(f"row:{rows}")
            if rows > galaxies[source][0] and rows < galaxies[dest][0]:
                num_row+=1
                # print("num_row+1")
            elif rows < galaxies[source][0] and rows > galaxies[dest][0]:
                num_row+=1
            else:
                num_row+=0
        num_col = 0
        for cols in col_no_galaxy:
            # print(f"col: {cols}")
            if cols > galaxies[source][1] and cols < galaxies[dest][1]:
                num_col+=1
                # print("num_col+1")
            elif cols < galaxies[source][1] and cols > galaxies[dest][1]:
                num_col+=1
            else:
                num_col+=0

        distance = abs(galaxies[source][1] - galaxies[dest][1])+(num_col*1) + abs(galaxies[source][0] - galaxies[dest][0])+(num_row*1)
        total_distance+=distance
        aged_distance = abs(galaxies[source][1] - galaxies[dest][1])+(num_col*999999) + abs(galaxies[source][0] - galaxies[dest][0])+(num_row*999999)
        aged_total_distance+=aged_distance

print(f"part 1: {total_distance}")        
print(f"part 2: {aged_total_distance}")
