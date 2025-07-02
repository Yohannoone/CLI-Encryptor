print('Hey Friend.' \
'Welcome to this CLI where you can encrypt messages and check the validity of your card number \n'
'you can choose what service will fit you. \n'
'1- Ceaser Cipher \n'
'2- Viginere Cipher \n'
'3- Check Card Number')

choosen_number = int(input('Pick one of these numbers'))
from ceaser import ceaser_cipher
if choosen_number == 1 :
    ceaser_cipher()
elif choosen_number == 2:
    print('Viginere Cipher')
elif choosen_number == 3:
    print('Check Card Number')
else:
    print('Naaah, try again.')
