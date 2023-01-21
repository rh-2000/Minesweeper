'''
NOTES:
most of this code was aided by the discord discussions for this task
'''

def mines_grid(grid):
    col_length = len(grid[0])
    row_length = len(grid)

# creating empty grid and initialising it with hash symbol
# 2D list being utilised
# first a list of '#' which is the same length as the no of columns in the grid
# second will print the above list the same number of times as there are rows in the grid
    new_grid = [["#" for x in range(col_length)] for y in range(row_length)]

# creating 2D list storing each direction ie 8 compass points in the format [row, column]
# to be used when checking the presence of mines in adjacent cells
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]

# nested loops going through each cell of the grid by row, column
    for row in range(row_length):
        for col in range(col_length):

            if grid[row][col] == "-":
                mine_count = 0
                # looping through each compass point to check against adjacent cells
                for point in directions:
                    adj_row = row + point[0]
                    adj_col = col + point[1]
                    # if statement to check two things:
                    # 1) to check if the adjacent cell is 'out of bounds' ie if it is beyond the original grid parameters
                    # 2) to check if the adjacent cell is a mine
                    if  (adj_row >= 0 and adj_row < row_length and adj_col >= 0 and adj_col < col_length) and (grid[adj_row][adj_col] == "#"):
                        mine_count += 1
                    # changing the values on the new grid from initialised hash to the given count (if applicable)
                new_grid[row][col] = mine_count
    
    return new_grid

# using the example grid given in the task
example_grid = [ ["-", "-", "-", "#", "#"],
                ["-", "#", "-", "-", "-"],
                ["-", "-", "#", "-", "-"],
                ["-", "#", "#", "-", "-"],
                ["-", "-", "-", "-", "-"] ]

example_output = mines_grid(example_grid)

print(example_output)