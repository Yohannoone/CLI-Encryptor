import time

# This function uses the Luhn algorithm to verify if a card number is valid.
def check_card(card_number):

    
    # The card number is reversed to start processing from the end—flipping it so the last digit comes first.
    rever_card_number = card_number[::-1]


    sum_even_numbers = 0
    sum_odd_numbers = 0


    # As we know, the Luhn algorithm adds the digits in the odd positions directly to the total sum—and that’s exactly what the code following this comment does.
    odd_numbers = rever_card_number[0::2]
    for digit in odd_numbers:
        sum_odd_numbers += int(digit)


    # For even digits, if doubling is under 10, keep it; if 10 or more, sum the digits—e.g., 11 becomes 2.
    even_numbers = rever_card_number [1::2]
    for digit in even_numbers:
       double_digit = int(digit) * 2
       if double_digit < 10:
           sum_even_numbers += double_digit
       elif double_digit >= 10:
           sum_g_ten = (double_digit // 10) + (double_digit % 10)
           sum_even_numbers += sum_g_ten


    # Now, add the total of odd and even sums together.
    sum_of_all = sum_odd_numbers + sum_even_numbers

    # Now, the modulo of the final sum determines validity: if it’s 0, the card is valid; otherwise, it’s invalid.
    if sum_of_all % 10 == 0:
        return 'Valid Card!'
    else:
        return 'is not Real, Maybe you got to double Check if you are writing it correctly'


# This function cleans input and checks if it’s valid before verification.
def luhn_handler():

    card_num = input('Enter you Card Number.')

    # The next lines act as a filter to remove spaces and dashes.
    card_key_translation = str.maketrans({' ' : '', '-' : ''})
    card_translated = card_num.translate(card_key_translation)

    # To make it user-friendly, I decided to add some flair to the code for the user.
    print(f'Checking card number: {card_translated}')
    time.sleep(1)
    print('Processing...')
    time.sleep(3)

    # This is the second filter: if the input contains no digits, it’s rejected.
    if not card_translated.isdigit():
        print('enter you card numbers, it is okay to includes spaces or -, other than you got to rewrite it.')
        return
    
    # The third filter rejects any  13 < numbers > 19.
    if len(card_translated) < 13:
        print('Your Number is shorter than normal.')
        return
    elif len(card_translated) > 19:
        print('That is too much for a Card number, try again')
        return
    
    return f'your Card Number is {card_translated} after cleaning it, and after checking it it turns that your Card {check_card(card_translated)}'