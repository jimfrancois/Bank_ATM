print('Welcome to python.hub Bank ATM')
restart = 'Y'
chances = 3
balance = 999.12

while chances >= 0:
    pin = int(input("Please Enter Your 4 Digit Pin: "))
    if pin == (1234):
        print('You entered your pin Correctly')
       

        while restart not in ('n', 'NO', 'no', 'N'):
            print('Please Press 1 For Your Balance')
            print('Please Press 2 To Make a withdrawl')
            print('Please Press 3 To Pay in')
            print('Please Press 4 To Return Card')

            option = int(input('What would you like to choose?: '))
            if option == 1:
                print('Your Balance is $', balance)
                restart = input('Would you like to go back? ')
                if restart in ('n', 'NO', 'no', 'N'):
                    print('Thank You')
                    #break
                #The Second Option
            elif option == 2:
                option = ('y')
                withdrawl = float(input('How Much would you like to withdraw? 10,20,40,60,80,100 for other enter 1: '
                                        ''))
                if withdrawl in [10, 20, 40.60, 80, 100]:
                    balance = balance - withdrawl
                    print("\nYour Balance is now $", balance)
                    restart = input('Would You like to go back? ')
                    if restart in ('n', 'NO', 'no', 'N'):
                        print('Thank You')
                        #break

                    elif withdrawl != [10, 20, 40.60, 80, 100]:
                        print('Invalid Amount, Please Re-try\n')
                        restart = ('y')
                    elif withdrawl == 1:
                        withdrawl = float(input('Please Enter desired amount: '))

                    #The Third Option.
            elif option == 3:
                Pay_in = float(input('Hom Much Would You Like To Pay In? '))
                balance = balance + Pay_in
                print('\nYour Balance is now $', balance)
                restart = input('Would you like to go back? ')
                if restart in ('n', 'NO', 'no', 'N'):
                    print('Thank You')
                    #break

                    #The Fourth Option.

            elif option == 4:
                print('Please wait while your card is Returned...\n')
                print('Thank you for your service.')
                #break

            else:
                print("Please Enter a correct number.\n")
                restart = ('y')

    elif pin != ('1234'):
        print('Incorrect password')
        chances = chances - 1
        if chances == 0:
            print('\nNo more tries')
            #break
