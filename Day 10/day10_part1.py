from collections import deque
#credits to shaunyuancw
with open('Day 10/input.txt', 'r') as file:
    field = []
    for line in file:
        
        field.append(line)
        
print(field)

def find_start(field):
    for i in range(len(field)):
        for j in range(len(field[i])):
            # print(field[i][j])
            if field[i][j]=="S":
                print("found")
                return (i,j)
start_position = find_start(field)
# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
#row, col
# Pipe Entries and respective exits
pipes = {
    '|': {'S': 'S', 'N': 'N'},
    '-': {'E': 'E', 'W': 'W'},
    'L': {'W': 'N', 'S': 'E'},
    'J': {'E': 'N', 'S': 'W'},
    '7': {'E': 'S', 'N': 'W'},
    'F': {'W': 'S', 'N': 'E'},
}

four_direction = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}
visited_positions = []
def is_valid(pos):
    return 0 <= pos[0] < len(field) and 0 <= pos[1] < len(field[0]) and field[pos[0]][pos[1]] != '.'

def get_possible_directions_from_start(matrix, start):
    # Check adjacent cells to find out which pipes are next to the start position
    possible_directions = []
    for dir in four_direction:
        new_pos = (start[0] + four_direction[dir][0], start[1] + four_direction[dir][1])
        if is_valid(new_pos) and matrix[new_pos[0]][new_pos[1]] in pipes:
            print(pipes[matrix[new_pos[0]][new_pos[1]]])
            if dir in pipes[matrix[new_pos[0]][new_pos[1]]]:
                possible_directions.append(dir)
    return possible_directions

def find_loop(matrix,start):
    is_part_of_loop = [['.' for _ in row] for row in matrix]
    
    path_length = 1
    current_pos = start
    visited = set([current_pos])

    # Determine the initial direction from the start position
    initial_directions = get_possible_directions_from_start(matrix, current_pos)

    is_part_of_loop[start[0]][start[1]] = 'L' # I'm lazy so manually identify
    next_dir = initial_directions[0] # Arbitrarily pick the first direction

    while True:        
        next_pos = (current_pos[0] + four_direction[next_dir][0], current_pos[1] + four_direction[next_dir][1])
        next_pipe = matrix[next_pos[0]][next_pos[1]]
        if next_pipe == 'S': # Found way back to start
            return path_length, is_part_of_loop
        
        next_dir = pipes[next_pipe][next_dir]

        if next_pos in visited: # Invalid loop
            return -1, None

        is_part_of_loop[next_pos[0]][next_pos[1]] = next_pipe
        visited.add(next_pos)
        path_length += 1
        current_pos = next_pos
def double_grid_resolution(original_grid):
    # The new grid will have twice the number of rows and columns
    new_rows = len(original_grid) * 2
    new_cols = len(original_grid[0]) * 2
    new_grid = [['.' for _ in range(new_cols)] for _ in range(new_rows)]
    
    # Define the mapping from pipe type to their doubled grid representation
    # (This will only add south and east connections; north and west will be handled by adjacent cells)
    pipe_mapping = {
        '|': [('|', '.'), ('|', '.')],
        '-': [('-', '-'), ('.', '.')],
        'L': [('L', '-'), ('.', '.')],
        'J': [('J', '.'), ('.', '.')],
        '7': [('7', '.'), ('|', '.')],
        'F': [('F', '-'), ('|', '.')],
        '.': [('.', '.'), ('.', '.')],
    }
    
    # Map each cell in the original grid to a 2x2 block in the new grid
    for row in range(len(original_grid)):
        for col in range(len(original_grid[0])):
            cell = original_grid[row][col]
            new_block = pipe_mapping[cell]
            
            new_grid[row * 2][col * 2] = new_block[0][0]
            new_grid[row * 2][col * 2 + 1] = new_block[0][1]
            new_grid[row * 2 + 1][col * 2] = new_block[1][0]
            new_grid[row * 2 + 1][col * 2 + 1] = new_block[1][1]
    
    return new_grid

def flood_fill(matrix, x, y, target, replacement):
    # Define the 8 possible movements (including diagonals)
    movements = [(-1, 0), (-1, 1), (0, 1), (1, 1), 
                 (1, 0), (1, -1), (0, -1), (-1, -1)]

    # Create a queue and enqueue the starting position
    queue = deque([(x, y)])
    
    # While the queue is not empty
    while queue:
        x, y = queue.popleft()
        
        # Continue if the position is out of bounds or the value is not the target
        if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]) or matrix[x][y] != target:
            continue
        
        # Replace the target value with the replacement value
        matrix[x][y] = replacement
        
        # Enqueue all 8 adjacent positions
        for dx, dy in movements:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and matrix[nx][ny] == target:
                queue.append((nx, ny))

def outer_flood_fill(matrix):
    rows, cols = len(matrix), len(matrix[0])
    
    # Flood fill from the edges including corners
    for y in range(cols):
        if matrix[0][y] == '.':
            flood_fill(matrix, 0, y, '.', 'X')
        if matrix[rows - 1][y] == '.':
            flood_fill(matrix, rows - 1, y, '.', 'X')
    for x in range(rows):
        if matrix[x][0] == '.':
            flood_fill(matrix, x, 0, '.', 'X')
        if matrix[x][cols - 1] == '.':
            flood_fill(matrix, x, cols - 1, '.', 'X')

def count_dot(matrix):
    inside_count = 0
    for row in range(0, len(matrix), 2):  # Only consider every second row
        for col in range(0, len(matrix[0]), 2):  # Only consider every second column
            # Check if all four sub-cells in the 2x2 block are '.'
            if (matrix[row][col] == '.' and 
                matrix[row][col+1] == '.' and 
                matrix[row+1][col] == '.' and 
                matrix[row+1][col+1] == '.'):
                inside_count += 1
    return inside_count


loop_found, is_part_of_loop = find_loop(field,start_position)
is_part_of_loop = double_grid_resolution(is_part_of_loop) # Double the grid resolution
outer_flood_fill(is_part_of_loop) # Flood fill 
        


print(f"Part 1: {int(loop_found/2)}")
print(f"Part 2: {count_dot(is_part_of_loop)}")


    
