# def inputString():
#     string1 = None
#     while not string1:
#         string1 = input('Please enter a string:')
#         try: 
#             int(string1)
#             print('Woops! That/s an integer, try again!')
#             break
#         except ValueError:
#             pass
#         try:
#             float(string1)
#             print('Woops! That/s a float, try again!')
#         except ValueError:
#             pass
#     return string1
# print(inputString())

def inputString():
    while True:
        string1 = input('Please enter a string:')
        try:
            float(string1)
            try: 
                int(string1)
                print('Woops! That\'s an integer, try again!')
            except:
                print('Woops! That\'s a float, try again!')
        except:
            return string1
print(inputString())