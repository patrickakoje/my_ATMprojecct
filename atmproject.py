name = input ('what is your name? \n')
allowedUsers = ['Seyi', 'Mike', 'Love']
allowedPassword = ['passwordSeyi', 'passwordMike', 'passwordLove']

if(name in allowedUsers):
    password = input ('Your Password? \n')
    userId = allowedUsers.index(name)

    if (password == allowedPassword [userId]):

        import datetime

        now = datetime.datetime.now()
        print(now.strftime('%d-%m-%y %H:%M:%S'))

        print('Welcome %s' % name)
        print('These are the available options')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Complaint')

        selectedOption = int(input ('Please select an Option \n'))

        if (selectedOption == 1):
            towithdraw = int (input ('How much would you like to withdraw? \n'))
            print('Take your cash')

        elif (selectedOption == 2):
            todeposit = int (input ('How much would you like to deposit? \n'))
            print('current balance')

        elif (selectedOption == 3):
            tocomplaint = input ('What issue would you like to report? \n')
            print('Thank you for contactng us')
        else:
            print('Password Incorrect,please try again')
else:
    print('Name not found, please try again')
    
