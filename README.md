# Minesweeper
A Python function that takes a grid of hashes (#) and dashes (-), where hashes represent mines and dashes represent mine-free spots, and returns a grid where each dash is replaced by a digit indicating the number of mines immediately adjacent to the spot.

## Usage
The mines_grid(grid) function takes a 2D list grid as input and returns a new 2D list where each dash is replaced by a digit indicating the number of mines immediately adjacent to the spot.

## Example
```
example_grid = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"]
]

example_output = mines_grid(example_grid)

print(example_output)

# Output:
# [
#     [1, 3, 3, "#", "#"],
#     [2, "#", 4, 4, 2],
#     [2, 4, "#", 4, 2],
#     [1, "#", "#", 3, 1],
#     [1, 2, 2, 2, 1]
# ]
```

## Implementation
The mines_grid function works by first creating a new grid of the same size as the input grid, where each cell is initialized with a hash symbol. It then loops through each cell in the input grid and checks if it is a dash. If it is, the function loops through each of the adjacent cells (in eight compass points) and counts the number of mines. Finally, it updates the corresponding cell in the new grid with the mine count.
