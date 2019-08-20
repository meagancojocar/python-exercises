# Lists 

backpack = []

backpack = [
        'drink bottle',
        'yoghurt',
        'headphones',
        'laptop',
]

backpack.append('blueberries')

# print(backpack[4])

backpack[0] = 'lunchbox'

# print(backpack)

# name = 'hayley'
# print(name[0])

# kinds of loops: for loop, while loop

for item in backpack:
    print(item)

# to ways to add an index
# for index,item in enumerate(backpack):
#     print(index,item)

# counter = 0
# for item in backpack:
#     print(counter, item)
#     counter = counter + 1

# counter = 0 
# while counter < len(backpack):
#     print(counter, backpack[counter])
#     counter = counter + 1

# exercise print 1 to 10

# count_to_ten = [
#     1,
#     2,
#     3,
#     4,
#     5,
#     6,
#     7,
#     8,
#     9,
#     10
# ]

# print 1-10 using a loop
count_to_ten = range(1,11)

# counter = 0
# while counter < len(count_to_ten):
#     print(count_to_ten[counter])
#     counter = counter + 1

# for number in count_to_ten:
#     print(number)

# num = 1
# while num <= 10:
#     print(num)
#     num += 1