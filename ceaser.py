import time

# This function takes the message from ceaser_handler and applies the input shift number for encryption.
def ceaser_cipher(message, shift_number):

    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_message = ''

    # This loop converts the message to lowercase, finds each letter's index, and adds the shift number—interesting, isn't it?
    for letter in message.lower():
        if letter == ' ':
            new_message += ' '
        elif letter in alphabet:
            index = alphabet.find(letter)
            new_index = (index + shift_number) % len(alphabet)
            new_letter = alphabet[new_index]
            new_message += new_letter
        else:
            new_message += letter
    return new_message

# This function takes the input message and the user's choice to encrypt or decrypt.
def ceaser_handler():
    inp_message = input('Write the message you want to encrypt.')
    # This ensures the input is a string and not digits.
    if not inp_message.isalpha():
        print('the Message should be letters not numbers or something else.')
        # Now, if the user enters numbers, return will stop the code from running further.
        return
    
    shift_inp = input('Write your shift number')
    # Ensures that if the input isn’t digits, the code stops to prevent errors from converting a string to int.
    if not shift_inp.isdigit():
        print('Do not write letters or something else, just numbers to shift your message.')
        return
    shift_inp_int = int(shift_inp)

    enc_dec = input('If you want to encrypt type 1, if decrypt type 2.')
    
    # Applies the same validation to the previous input.
    if not enc_dec.isdigit():
        print('Do not write letters or something else, just 1 or 2.')
        return
    enc_dec_int = int(enc_dec)

    # To make it user-friendly, I decided to add some flair to the code for the user.
    print(f'Your message is {inp_message}, and you decide to shift it with {shift_inp}, and your Numcryption is {enc_dec}')
    time.sleep(2)
    print('Processing...')
    time.sleep(3)

    # This one handles the shift input and directs whether to encrypt or decrypt.
    if enc_dec_int == 1:
        final_shift = shift_inp_int * 1
    elif enc_dec_int == 2:
        final_shift = shift_inp_int * -1
    else:
        print('Naaaaaah that is wrong ')
    
    return f' the result is {ceaser_cipher(inp_message, final_shift)}, see you in other enc or dec.'