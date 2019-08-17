# TASK 1
# given a 5x5 grid, add the last column and row, then flip the card at the
# coordinate specified by the user

five_by_five_grid = [
    ['X','0','X','X','X'],
    ['X','X','0','0','0'],
    ['X','0','X','0','X'],
    ['0','X','X','X','X'],
    ['X','0','0','X','X'],
]

# first step is to add colum 6 and row 6

for row in five_by_five_grid:
    x_counter = 0 
    for char in row:
        if char == "X":
            x_counter +=1


# for row in five_by_five_grid:


# five_by_five_grid.append('X')

# output the grid to the user
# for card in five_by_five_grid:
#     print(card)

# # ask the user for the coordinate of the card to flip
# message = input('What coordinate of card would you like to flip: ')

# # message..strip('()')

# print(five_by_five_grid)

# e.g. input could be: (0,2)

# output the grid with the flipped card

## TASK 2

# given a six by six grid, work out what card was flipped

# your program should output the coordinate of the flipped card
# in this case it would be: (x,y)