def viginer_cipher(message, key, enc_dec):
  

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_message = ''
    key_plus = 0
    for letter in message.lower():
        # The first component loops through the shift_message so that it continues throughout the entire message.
        shift_index_key = key[ key_plus % len(key)]
        
        # Use an if condition to check whether letter is in alphabet. If true, process it; otherwise, skip to the next iteration.
        if letter in alphabet.lower():

            # After looping the key, it's time to find the new letter's index.
            key_plus += 1
            num_index = alphabet.find(shift_index_key) 
            letter_index = alphabet.find(letter)
            new_letter_index = ((num_index *  enc_dec)  + letter_index) % len(alphabet)
            new_letter = alphabet[new_letter_index]
            new_message += new_letter

        # If the character isn't in the alphabet, check if it's a space. If so, append it as-is.
        elif letter == ' ':
            new_message += ' '

        # If neither of the previous conditions are met, it's most likely a punctuation mark or a number, so leave it unchanged.
        else:
            new_message += letter
 
    return new_message

def viginer_handler():
    # Obtain the message input for encryption or decryption.
    message = input('Write the message you want to encrypt')
    # Two choices: 1 for encryption, 2 for decryption (using * -1). Otherwise, it does nothing but prints the message inside the else block.
    key_mess = input('Write the key for encryption or decryption.')
    # I used .lower() to make the key flexible—without it, the code would break if the user enters an uppercase letter.
    key_mess = key_mess.lower()
    # Asking for the choice of user if he wants to enc or dec.
    if not key_mess.isalpha():
        print('the key should be letters not numbers or something else.')
        return
    type_enc = int(input('if you want to encrypt press 1, if you to decrypt press 2.'))
    if type_enc == 1:
        direction =  1
    elif type_enc == 2:
        direction = -1
    # This informs the user not to use numbers; if they do, they should choose letters instead.
    else:
        print('chooose just 1 or 2.')
    return viginer_cipher(message, key_mess, direction)


print(viginer_handler())    