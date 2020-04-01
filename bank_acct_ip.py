welcome = 'Welcome to Stubinski Bank! Please choose from the following options.'
leave = 'Thank you for visiting Stubinski Bank, have a wonderful day!'

login_menu = ['1. Login',
              '2. Create Account',
              '3. Exit'
              ]

main_menu = ['1. View Balance',
             '2. Deposit',
             '3. Withdrawal',
             '4. Change Password',
             '5. Logout'
             ]

balance = float(0)

login_screen = True

main_screen = True

userLoginChoice = ''

userName = ''

userPassword = ''

userMainMenuChoice = ''


def displayLoginMenu():
    print(login_menu[0])
    print(login_menu[1])
    print(login_menu[2])


def displayMainMenu():
    print(main_menu[0])
    print(main_menu[1])
    print(main_menu[2])
    print(main_menu[3])
    print(main_menu[4])


def changePwd(old_pwd, new_pwd):
    if (old_pwd == userPassword and new_pwd != userPassword):
        print('Your password was changed successfully!')
    else:
        print('New password must be different than current password!')


# print welcome message
print(welcome)

while login_screen == True:

    displayLoginMenu()

    # ask user for their login menu choice
    userLoginChoice = input()

    # if user chooses Login, ask user for credentials
    if (userLoginChoice == '1'):
        print('Enter your credentials to login.')
        login_id = input('Please enter your username: ')
        login_pwd = input('Please enter your password: ')

        if (login_id == userName and login_pwd == userPassword):
            print('Welcome to your account!')
            login_screen = False

        else:
            print('Username or password is incorrect.')

    # if user chooses Create Account
    elif (userLoginChoice == '2'):
        print('Please choose a username and password.')
        userName = input('Please enter a username: ')
        userPassword = input('Please enter a password: ')

    # if user chooses Exit
    else:
        print(leave)
        login_screen = False

while main_screen == True:

    displayMainMenu()

    userMainMenuChoice = input()

    # 1 for balance
    if (userMainMenuChoice == '1'):
        print(f'Your balance is ${balance}')

    # deposit
    elif (userMainMenuChoice == '2'):
        try:
            userDeposit = input('How much would you like to deposit? ')
            balance += float(userDeposit)
        except ValueError:
            print('Please enter a valid number.')

    # withdrawal
    elif (userMainMenuChoice == '3'):
        try:
            userWithdrawal = input('How much would you like to withdraw? ')
            balance -= float(userWithdrawal)
        except ValueError:
            print('Please enter a valid number.')

    # change pwd
    elif (userMainMenuChoice == '4'):
        current_pwd = input('Please enter your current password: ')
        new_pwd = input(
            'Please enter your new password. It cannot be the same as your existing password: '
        )
        changePwd(current_pwd, new_pwd)
        userPassword = new_pwd
        print('current password: ' + userPassword)

    # logout
    else:
        print(leave)
        main_screen = False
