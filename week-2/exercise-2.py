# # TASK 1
# --- Instruction: given a 5x5 grid, add the last column and row, then flip the card at the coordinate specified by the user

five_by_five_grid = [
    ['X','0','X','X','X'],
    ['X','X','0','0','0'],
    ['X','0','X','0','X'],
    ['0','X','X','X','X'],
    ['X','0','0','X','X'],
]

# --- Instruction: first step is to add colum 6 and row 6

x_counter = 0
for row in five_by_five_grid:
    for col in row:
        if col == 'X':
            x_counter +=1
    if x_counter % 2 == 0:
        row.append('0')
    else:
        row.append('X')


five_by_five_grid.append(['0','X','0','X','0','X'])

six_by_six_grid = five_by_five_grid

# --- Instruction: output the grid to the user
for row in five_by_five_grid:
    print(row)

# --- Instruction: ask the user for the coordinate of the card to flip e.g. input could be: (0,2)
message = input('What coordinate of card would you like to flip: ')

x = int(message[1])
y = int(message[3])

if six_by_six_grid[y][x] == 'X':
    six_by_six_grid[y][x] == '0'
else: 
    six_by_six_grid[y][x] == 'X'

# --- Instruction: output the grid with the flipped card
for row in six_by_six_grid:
    print(row)

## TASK 2

# --- Instruction: given a six by six grid, work out what card was flipped
# your program should output the coordinate of the flipped card
# in this case it would be: (x,y)