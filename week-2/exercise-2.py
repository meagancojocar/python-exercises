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
    for char in row:
        if char == 'X':
            x_counter +=1
    if x_counter % 2 == 0:
        row.append('0')
    else:
        row.append('X')


five_by_five_grid.append(['0','X','0','X','0','X'])
    
# --- Instruction: output the grid to the user
print(five_by_five_grid)


# --- Instruction: ask the user for the coordinate of the card to flip e.g. input could be: (0,2)
message = input('What coordinate of card would you like to flip: ')

message.strip('()')


# --- Instruction: output the grid with the flipped card

## TASK 2

# --- Instruction: given a six by six grid, work out what card was flipped
# your program should output the coordinate of the flipped card
# in this case it would be: (x,y)