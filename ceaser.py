def ceaser_cipher(message, shift_number):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_message = ''
    for letter in message.lower():
        if letter == ' ':
            new_message += ' '
        else:
            index = alphabet.find(letter)
            new_index = (index + shift_number) % len(alphabet)
            new_letter = alphabet[new_index]
            new_message += new_letter
    return new_message

translted = 'AAA'
print(ceaser_cipher(translted, 3))