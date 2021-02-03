def CheckValidNumber(card_number):
    check_digit = card_number.pop()    
    first_digit = card_number[0]
    second_digit = card_number[1]

    card_number.reverse()
    
    processed_digits = []

    for index, digit in enumerate(card_number):
        if index % 2 == 0:
            doubled_digit = int(digit) * 2
		
            if doubled_digit > 9:
                doubled_digit = doubled_digit - 9

            processed_digits.append(doubled_digit)
        else:
            processed_digits.append(int(digit))

    total = int(check_digit) + sum(processed_digits)


    if total%10 == 0  and  13<=len(card_number)<=16  and  (first_digit in (4,5,6)  or first_digit,second_digit == 3,7 )   :
        return True
    else:
        return False

