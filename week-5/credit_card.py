## --- Instruction: calculate check digit 
def calculate_credit_card_check_digit(card_number):
    list_of_digits = list(card_number[::-1])
    sum = 0
    for digit in range(0,len(list_of_digits)):
        if digit % 2 == 0:
            digit_times_two = int(list_of_digits[digit]) * 2
            if digit_times_two > 9:
                sum += digit_times_two - 9
            else:
                sum += digit_times_two
        else:
            sum += int(list_of_digits[digit])
    sum = str(sum * 9)
    return sum[(len(sum) - 1)]

## --- Instruction: Should return 5 if card_number = 542418027979176    
print(calculate_credit_card_check_digit('542418027979176'))    

## --- Instruction: Check the check digit number to see if a value credit card number 
def check_credit_card_check_digit(card_number):
    check_digit = int(card_number[(len(card_number) - 1)])
    correct_check_digit = int(calculate_credit_card_check_digit(card_number[:(len(card_number) - 1)]))
    if check_digit == 0 and correct_check_digit == 10:
        return ('This credit card number is valid.')
    elif check_digit != 0 and correct_check_digit == check_digit:
        return ('This credit card number is valid.')
    else:
        return ('This credit card number is invalid.')

print(check_credit_card_check_digit('5424180279791765'))