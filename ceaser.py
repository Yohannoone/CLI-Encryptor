def ceaser_cipher(message, shift_number):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_message = ''
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

def ceaser_handler():
    inp_message = input('Write the message you want to encrypt.')
    shift_inp = int(input('Write your shift number'))
    enc_dec = int(input('If you want to encrypt type 1, if decrypt type 2.'))
    if enc_dec == 1:
        final_shift = shift_inp * 1
    elif enc_dec == 2:
        final_shift = shift_inp * -1
    else:
        print('Naaaaaah that is wrong ')
    print(ceaser_cipher(inp_message, final_shift))

ceaser_handler()

