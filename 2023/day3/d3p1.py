import re
from collections import deque

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

# Pass as a grid

grid = []

for line in lines:
    grid.append(list(line))

rows, cols = len(grid), len(grid[0])

list_of_nums = []
visited = set()

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
            if not grid[nr][nc].isnumeric() and grid[nr][nc] != ".":
                return True
    return False
    
def search(grid, r, c):
    is_special = check(grid, r, c)

    if is_special:
        num_str = grid[r][c]
        r_save = r
        c_save = c
        
        while (c-1 >= 0 and grid[r][c-1].isnumeric()):
            num_str = grid[r][c-1] + num_str
            c -= 1

        r = r_save
        c = c_save

        while (c+1 < cols and grid[r][c+1].isnumeric()):
            num_str += grid[r][c+1]
            visited.add((r, c+1))
            c += 1

        list_of_nums.append(int(num_str))

for r in range(rows):
    for c in range(cols):
        if grid[r][c].isnumeric() and (r, c) not in visited:
            search(grid, r, c)

print(sum(list_of_nums))
# print(list_of_nums)

