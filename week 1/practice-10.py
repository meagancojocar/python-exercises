def getInt():
    num1 = None
    while not num1:
        try:
            num1 = int(input('Please enter an integer: '))
        except:
            print('Woops! That\'s not an integer, try again!')
    return num1

def multiplyByTen(num1):
    return num1 * 10

print(multiplyByTen(getInt()))