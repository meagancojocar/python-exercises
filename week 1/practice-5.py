def compare(num1,num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2 
    else:
        return 'The numbers are the same'
    
print(compare(6,3))
print(compare(34,48))
print(compare(123,123))