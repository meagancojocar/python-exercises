# def largerThanFive(num1):
#     if num1 > 5:
#         return True
#     elif 5 > num1:
#         return False
#     else: 
#         return if num1 =='The integer is exactly 5.'

def largerThanFive(num1):
    if num1 == 5: 
        return 'The integer is exactly 5.'
    return num1 > 5 

print(largerThanFive(10))
print(largerThanFive(1))
print(largerThanFive(5))