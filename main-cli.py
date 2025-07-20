import time
print('Hey My Friend.\n'
    'Welcome to this CLI where you can encrypt and decrypt messages and check the validity of your card number \n'
     'you can choose what service will fit you. \n'
     '1- Ceaser Cipher 🔐 \n'
     '2- Viginere Cipher 🧠 \n'
     '3- Check Card Number 💳')
while  True:
   

    choosen_number = input('Pick one of these numbers or you can quit with pressing *q*.')
    if choosen_number.isdigit():
        number = int(choosen_number)
        if number == 1 :
           from ceaser import ceaser_handler
           print(ceaser_handler())
           break

        elif number == 2:
            from viginer import viginer_handler
            print(viginer_handler())
            break

        elif number == 3:
            from luhn import luhn_handler
            print(luhn_handler())
            
            break

        else:
            print('Naaah, try again.')
    
    elif choosen_number == 'q':
        time.sleep(2)
        print('Good Bye 👋 My Friend, See you later.')
        break
