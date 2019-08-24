## --- Instruction: calculate check digit 
def calculate_credit_card_check_digit(card_number):
    list_of_digits = list(card_number[::-1])
    doubled = 0
    total = 0
    for digit in list(range(0,len(list_of_digits))):
        if digit % 2 == 0:
            digit_times_two = int(list_of_digits[digit]) * 2
            if digit_times_two > 9:
                total += (digit_times_two - 9)
            else:
                total += digit_times_two
        else:
            total += digit_times_two
    total = str(total * 9)
    return str(total[(len(total) - 1)])
    
# print(calculate_credit_card_check_digit('401200003333002'))    

## --- Instruction: Check the check digit number to see if a value credit card number 
def check_credit_card_check_digit(card_number):
    check_digit = int(card_number[(len(card_number) - 1)])
    correct_check_digit = int(calculate_credit_card_check_digit(card_number[:(len(card_number) - 1)]))
    if check_digit == 0 and correct_check_digit == 10:
        return ('This credit card number is valid.')
    elif check_digit != 0 and correct_check_digit == check_digit:
        return ('This credit card number is valid')
    else:
        return ('This credit card number is invalid.')

