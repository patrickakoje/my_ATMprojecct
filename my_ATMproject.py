#ATMproject

import random
import datetime



database = {}

def init():
    
    print('Welcome to Zuri Trust Bank')

    haveAccount = int(input ('Do you have an account with us: 1.(yes) 2.(no)\n'))
    if (haveAccount == 1):
        login()
    elif (haveAccount == 2):
        openAccount = int(input ('Do you want to open an account with us: 1.(yes) 2.(no)\n'))
        if (openAccount == 1):
           register()
        if (openAccount == 2):
            init()

    else:
            print('You have selected an invalid Option. Please try again')

            init()

def login():
    print('********** Login **********')
    isLoginSuccesful = False

    while isLoginSuccesful == False:
        accountNmberFromUser = int(input ('Enter your Account Number\n'))
        password = input('Enter your password\n')   
        for accountNumber,userDetails in database.items():
            if(accountNumber == accountNmberFromUser):
                if(userDetails[3] == password):
                    print('You have logged in Sucessfully')
                    isLoginSuccesful = True
                    bankOperation(userDetails)
                else:                             
                    print('Invalid account or password. Please try again')
    

def register():
    print('********** Register **********')

    email = input('Please enter your email address:\n')
    first_name = input('Please enter your first name:\n')
    last_name = input('Please enter your last name:\n')
    password = input('Please create a password:\n')

    accountNumber = generationAccountNumber()

    database[accountNumber]=[first_name, last_name, email, password]

    print('Your account has been created successfully')
    print('**************************************************')
    print('Your acccount number is: %d' % accountNumber)
    print('Please keep your account details safe')
    print('*************************************************')

    login()

def bankOperation(user):
    print('Welcome %s %s' % (user[0],user[1]))

    now = datetime.datetime.now()
    print(now.strftime('%d-%m-%y %H:%M:%S'))

    selectedOption = int(input('what would you like to do? 1. deposit 2. withdrawal 3. complaint 4.logout\n'))
    if(selectedOption == 1):
        depositOperation()

    if(selectedOption == 2):
        withdrawalOperation()

    if(selectedOption == 3):
        complaintOperation()
    
    if(selectedOption == 4):
        logout()
    
    else:
        print("Invalid Option selected. Please try again")
    
    bankOperation(user)

def depositOperation():
    todeposit = int (input ('How much would you like to deposit? \n'))
    print('You have sucessfully deposited %d' % todeposit)
    
    login()
        
def withdrawalOperation():
    towithdraw = int (input ('How much would you like to withdraw? \n'))
    print('You have sucessfully withdrawn %d' % towithdraw)

    login()

def complaintOperation():
    tocomplaint = input ('What issue would you like to report? \n')
    print('Thank you for contactng us')

    login()
    
def logout():
    
    login()


def generationAccountNumber():
    return random.randrange(1111111111,9999999999)



init()
