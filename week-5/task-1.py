def calculate_credit_card_barcode_check_digit(card_number):
    if len(card_number) == 12:
        sum = card_number[0] + card_number[1] + card_number[2] + card_number[3] + card_number[4] + card_number[5] + card_number[6]
        sum = int(sum)
        check_digit = (10 - (sum % 10)% 10)
        return check_digit
    elif len(card_number) == 13:

    else:
        return 'This is a valid credit card code'



print(calculate_credit_card_barcode_check_digit('9400550619775'))
    