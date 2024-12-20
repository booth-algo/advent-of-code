import re
from collections import defaultdict

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

# Pass as a grid

grid = []

for line in lines:
    grid.append(list(line))

rows, cols = len(grid), len(grid[0])

visited = set()
gear_map = {}

directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1)
] # 8 adjacent positions

def check(grid, r, c):
    # Check for adjacent special symbol
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]): # bounds check
            if grid[nr][nc] == '*':
                return (nr, nc)
    return None
    
def search(grid, r, c):
    is_special = check(grid, r, c)
    r_save = r
    c_save = c

    if is_special is not None:
        num_str = grid[r][c]
        
        while (c-1 >= 0 and grid[r][c-1].isnumeric()):
            num_str = grid[r][c-1] + num_str
            c -= 1

        r = r_save
        c = c_save

        while (c+1 < cols and grid[r][c+1].isnumeric()):
            num_str += grid[r][c+1]
            visited.add((r, c+1))
            c += 1

        if is_special in gear_map.keys():
            gear_map[is_special].append(num_str)
        else:
            gear_map[is_special] = [num_str]

for r in range(rows):
    for c in range(cols):
        if grid[r][c].isnumeric() and (r, c) not in visited:
            search(grid, r, c)

gear_ratio = 0

for key, val in gear_map.items():
    if len(gear_map[key]) == 2:
        temp = 1
        temp = int(gear_map[key][0]) * int(gear_map[key][1])
        gear_ratio += temp

print(gear_ratio)

