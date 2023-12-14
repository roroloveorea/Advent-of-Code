from itertools import groupby
#credits to shaunyuencw
def count_arrangements_iterative(spring_pattern, group_sizes):

    def is_valid_combination(pattern, group_sizes):
        groups = [len(list(g)) for k, g in groupby(pattern) if k == '#'] # Count the number of damaged springs in each group
        return groups == group_sizes # Check if the groups match the required sizes

    stack = [(0, '')]
    valid_combinations = 0

    while stack:
        idx, current_pattern = stack.pop()

        if idx == len(spring_pattern): # Reached the end of the springs pattern
            if is_valid_combination(current_pattern, group_sizes):
                valid_combinations += 1 # Found a valid combination
        else:
            if spring_pattern[idx] == '?': 
                # Try both possibilities for unknown springs
                stack.append((idx + 1, current_pattern + '.')) 
                stack.append((idx + 1, current_pattern + '#'))
            else:
                # Add the current spring to the pattern
                stack.append((idx + 1, current_pattern + spring_pattern[idx]))

    return valid_combinations

rows = []
def duplicate_springs(spring, arrangements):
    new_spring = spring*5
    new_arr = arrangements*5
    return new_spring, new_arr
with open('Day 12/input.txt', 'r') as file:
    for line in file:
        springs, arrangements = line.strip().split(' ')
        arrangements = [int(val) for val in arrangements.split(',')]
        springs, arrangements = duplicate_springs(springs, arrangements)

        
        rows.append((springs, arrangements))
        # print(rows)

part1 = sum(count_arrangements_iterative(pattern, group_sizes) for pattern, group_sizes in rows)
print(f"Part 1: {part1}")

