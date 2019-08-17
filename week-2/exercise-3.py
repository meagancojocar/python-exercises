

people = {
    'hayley': 'lead instructor',
    'nanwen': 'wears shirt'
}

people['chloe'] = 'wears glasses'
people['hayley'] = 'wears red'


# --- TASK 1: use a for loop to print out each key and value in a dictionary

# --- My solution using google 

# for person,key in people.items():
#     print(person+': '+key) 

# --- Hayleys solution

# for person in people:
#     print(person+': '+people[person])

# --- TASK 2: given a list of names create a dictonary where the key is the first index and the value is the name

# names = ['chloe','cass','sarah','ellie','maddy']
# dict_names = dict(enumerate(names))
# print(dict_names)

# --- TASK 3: given a list of tuples, create a dictionary where the key is the first value in the tuple and the value is the second

people = [
    ('chloe', 'wears glasses'),
    ('maddy', 'is sitting next to beverly'),
    ('cass', 'is online'),
    ('marc', 'is a mentor')
]

dict_people = dict(people)
print(dict_people)