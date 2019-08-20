# def levelUp(name, age):
#     if age > 30:
#         return name+' is at level '+str(age)
#     elif 30 > age:
#         return name+' is '+str(age)+' years old'
#     else: 
#         return name+' is '+str(age)+'!!!'

# print(levelUp('Hayley', 22))
# print(levelUp('Sally',52))
# print(levelUp('Josh',30))

def levelUp(name, age):
    if age > 30:
        return '{name} is at level {age}'.format(name=name, age=age)
    elif 30 > age:
        return '{name} is {age} years old'.format(name=name, age=age)
    else: 
        return '{name} is {age} !!!'.format(name=name, age=age)

print(levelUp('Hayley', 22))
print(levelUp('Sally',52))
print(levelUp('Josh',30))