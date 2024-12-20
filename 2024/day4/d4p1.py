
'''
Idea:

For every character in the graph, see if the entry is an X.
If the entry is an X, scan for the neighbouring 8 characters:

...
.X.
...

If any of them is an M, then we continue on that direction. 
e.g. if X is at position (i,j), and M is at position (i+1, j+1),
then we continue search (i+1, j+1) for A.
Remember to handle out of bound cases.

'''

def search(grid, row, col):
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    neighbours = []
    count = 0
    height = len(grid)
    width = len(grid[0])

    for dx, dy in directions:
        new_row = row + dx
        new_col = col + dy

        if 0 <= new_row < height and 0 <= new_col < width:
            if grid[new_row][new_col] == 'M':
                neighbours.append((new_row, new_col, dx, dy))
    
    for entry in neighbours:
        new_row = entry[0]
        new_col = entry[1]
        dx = entry[2]
        dy = entry[3]
        a_row = new_row + dx
        a_col = new_col + dy
        s_row = a_row + dx
        s_col = a_col + dy

        if 0 <= a_row < height and 0 <= a_col < width and 0 <= s_row < height and 0 <= s_col < width:
            if grid[a_row][a_col] == 'A' and grid[s_row][s_col] == 'S':
                count += 1

    return count


with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

grid = []
count = 0

for line in lines:
    text = [char for char in line]
    grid.append(text)

for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == 'X':
            count += search(grid, row, col)

print(count)