with open("test_input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

grid = []
count = 0

for line in lines:
    text = [char for char in line]
    grid.append(text)

def search(grid, row, col):

    height = len(grid)
    width = len(grid[0])
    
    diagonals = [
        ((-1,-1), (1,1)), # pair 1
        ((-1,1), (1,-1)) # pair 2
    ]

    diagonal_patterns = []

    for m_dir, s_dir in diagonals:
        m_row, m_col = row + m_dir[0], col + m_dir[1]
        s_row, s_col = row + s_dir[0], col + s_dir[1]

        if (0 <= m_row < height and 0 <= m_col < width and 
            0 <= s_row < height and 0 <= s_col < width):
            
            pattern1 = (grid[m_row][m_col] == 'M' and grid[s_row][s_col] == 'S')
            pattern2 = (grid[m_row][m_col] == 'S' and grid[s_row][s_col] == 'M')
            diagonal_patterns.append(pattern1 or pattern2)
        else:
            diagonal_patterns.append(False)

    # diagonal_pattern is simply a 2-entry array, where both pairs have to 
    # satisfy a S-A-M or M-A-S format. The 2 patterns refer to the two possibilities,
    # and the two entries refer to testing both diagonals 

    return 1 if all(diagonal_patterns) else 0

for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == 'A':
            count += search(grid, row, col)

print(count)