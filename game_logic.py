import random

# funtion to create a new game with n tiles on it
def new_game(n):
    grid = [[0] * n for _ in range(n)]
    add_new_tile(grid)
    add_new_tile(grid)
    return grid

# logic to randomly add 2 or 4 in the grid. It will run until it finds an empty space and then add a value
def add_new_tile(grid):
    row = random.randint(0,len(grid)-1)
    col = random.randint(0,len(grid[0])-1)
    while grid[row][col] != 0:
        row = random.randint(0, len(grid)-1)
        col = random.randint(0,len(grid[0])-1)
    grid[row][col] = 2 if random.random() < 0.9 else 4

# the 4 main logic movements are compress, merge, reverse and transpose. Each one will recive the grid in a specific state
    # and modify it based on it.

def compress(grid):
    new_grid = [[0 for _ in range(len(grid))] for _ in range(len(grid))]
    for i in range(len(grid)):
        pos = 0
        for j in range(len(grid)):
            if grid[i][j] != 0:
                new_grid[i][pos] = grid[i][j]
                pos += 1
    return new_grid

def merge(grid):
    for i in range(len(grid)):
        for j in range(len(grid)-1):
            if grid[i][j] == grid[i][j+1] and grid[i][j] != 0:
                grid[i][j] = grid[i][j] * 2
                grid[i][j+1] = 0
    return grid

def reverse(grid):
    new_grid = []
    for i in range(len(grid)):
        new_grid.append([])
        for j in range(len(grid)):
            new_grid[i].append(grid[i][len(grid)-j-1])
    return new_grid

def transpose(grid):
    new_grid = [[0 for _ in range(len(grid))] for _ in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid)):
            new_grid[i][j] = grid[j][i]
    return new_grid

def move_left(grid):
    new_grid = compress(grid)
    new_grid = merge(new_grid)
    new_grid = compress(new_grid)
    return new_grid

def move_right(grid):
    new_grid = reverse(grid)
    new_grid = move_left(new_grid)
    new_grid = reverse(new_grid)
    return new_grid

def move_up(grid):
    new_grid = transpose(grid)
    new_grid = move_left(new_grid)
    new_grid = transpose(new_grid)
    return new_grid

def move_down(grid):
    new_grid = transpose(grid)
    new_grid = move_right(new_grid)
    new_grid = transpose(new_grid)
    return new_grid

# check if there is spaces left 
def check_game_over(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return False
            if j < len(grid[0])-1 and grid[i][j] == grid[i][j+1]:
                return False
            if i < len(grid)-1 and grid[i][j] == grid[i+1][j]:
                return False
    return True

# console implementation for testing :)
def print_grid(grid):
    for row in grid:
        print("\t".join([str(cell) for cell in row]))
    print()