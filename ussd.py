acct_bal = 1_000_000_000.00
airtime_bal = 0.0
data_bal = 0.0

# Function for buying airtime from bank
def bank_airtime():
    global airtime_bal
    global acct_bal
    airtime_purchase = int(input('How much airtime are you purchasing? '))
    # checking if the airtime to purchase is less than acct number
    if airtime_purchase > acct_bal:
        print(f'Sorry {name}, insuffient funds, your account balance is #{acct_bal}')
        airtime_purchase = int(input('How much airtime are you purchasing? '))
        if airtime_purchase <= acct_bal:
            airtime_bal += airtime_purchase
            acct_bal -= airtime_purchase
            print(f'Hello {name}, you have successfully purchased N{airtime_purchase} airtime and your account balance is N{airtime_bal}')

    else:
        airtime_bal += airtime_purchase
        acct_bal -= airtime_purchase
        print(f'Hello {name}, you have successfully purchased N{airtime_purchase} airtime and your airtime balance is N{airtime_bal}')
    start = 1
    while start == 1:
        # Asking if another transaction is going to be carried out
        choice = input('Are you willing to carry another transction(yes/no)? ').lower()
        if choice == 'yes':
            bank_airtime()
            break
        elif choice == 'no':
            menu()
            break
        else:
            start = 1
            while start == 1:
                print('Please enter a correct input(yes/no)')
                choice = input('Are you willing to carry another transction(yes/no)? ').lower()
                if choice == 'yes':
                    bank_airtime()
                    break
                elif choice == 'no':
                    menu()
                    break
            start += 1
    start += 1


# Function for buying data from bank
def bank_data():
    global acct_bal
    global data_bal
    data_purchase = int(input('How many GB are you purchasing? '))
    # Checking if there is suffient funds in the bank account
    if data_purchase > acct_bal:
        print(f'Sorry {name}, insuffient funds, your account balance is #{acct_bal}')
        data_purchase = int(input('How many GB are you purchasing? '))
        if data_purchase <= acct_bal:
            data_bal += data_purchase
            acct_bal -= data_purchase
            print(f'Hello {name}, you have successfully purchased {data_purchase} GB data and your data balance is {data_bal} GB')

    else:
        data_bal += data_purchase
        acct_bal -= data_purchase
        print(f'Hello {name}, you have successfully purchased {data_purchase} GB data and your data balance is {data_bal} GB')
    start = 1
    while start == 1:
        choice = input('Are you willing to carry another transction(yes/no)? ').lower()
        if choice == 'yes':
            bank_data()
            break
        elif choice == 'no':
            menu()
            break
        else:
            start = 1
            while start == 1:
                print('Please enter a correct input(yes/no)')
                choice = input('Are you willing to carry another transction(yes/no)? ').lower()
                if choice == 'yes':
                    bank_data()
                    break
                elif choice == 'no':
                    menu()
                    break
            start += 1
    start += 1


# Function for buying data from airtime balance
def airtime_bal_buy():
    print('\n')
    data_purchase = int(input('How many GB are you purchasing? '))
    global airtime_bal
    global data_bal
    if data_purchase > airtime_bal:
        # Checking if there is sufffient funds
        print(f'Sorry {name}, you do not have suffcient airtime, your airtime balance is N{airtime_bal}')
        data_purchase = int(input('How many GB are you purchasing? '))
        if data_purchase <= airtime_bal:
            data_bal += data_purchase
            airtime_bal -= data_purchase
            print(f'Hello {name}, you have successfully purchased {data_purchase} GB data and your data balance is {data_bal} GB')
    else:
        data_bal += data_purchase
        airtime_bal -= data_purchase
        print(f'Hello {name}, you have successfully purchased {data_purchase} GB data and your data balance is {data_bal} GB')
    start = 1
    while start == 1:
        choice = input('Are you willing to carry another transction(yes/no)? ').lower()
        if choice == 'yes':
            airtime_bal_buy()
            break
        elif choice == 'no':
            menu()
            break
        else:
            start = 1
            while start == 1:
                print('Please enter a correct input(yes/no)')
                choice = input('Are you willing to carry another transction(yes/no)? ').lower()
                if choice == 'yes':
                    airtime_bal_buy()
                    break
                elif choice == 'no':
                    menu()
                    break
            start += 1
    start += 1



# function for gifting airtime
def gifting_airtime():
    global airtime_bal
    print('Note: It will be deducted from your airtime balance')
    phone_no = input('Please enter your phone number: ')
    if len(phone_no) != 11:
        start = 1
        while start == 1:
            print('Phone number must be 11 digit')
            phone_no = input('Please enter a valid phone number: ')
            if len(phone_no) == 11:
                break
        start += 1
    rep_phone_no = input("Please enter recipient's phone number: ")
    if len(rep_phone_no) != 11:
        start = 1
        while start == 1:
            print('Phone number must be 11 digit')
            rep_phone_no = input('Please enter a valid phone number: ')
            if len(rep_phone_no) == 11:
                break
        start += 1
    if phone_no == rep_phone_no:
        start = 1
        while start == 1:
            rep_phone_no = input("Please enter a phone number different from your's: ")
            if rep_phone_no != phone_no:
                break
        start += 1
        if len(rep_phone_no) != 11:
            start = 1
            while start == 1:
                print('Phone number must be 11 digit')
                rep_phone_no = input('Please enter a valid phone number: ')
                if len(rep_phone_no) == 11:
                    break
            start += 1
    gift_airtime = int(input('How much airtime are you gifting? '))
    if gift_airtime > airtime_bal:
        start = 1
        while start == 1:
            print(f'Sorry {name}, your airtime balance is {airtime_bal}')
            gift_airtime = int(input('How much airtime are you gifting? '))
            if gift_airtime <= airtime_bal:
                airtime_bal -= gift_airtime
                print(f'Hello {phone_no}, you have successfully gifted N{gift_airtime} to {rep_phone_no}, your airtime balance is N{airtime_bal}')
                break
        start += 1
    airtime_bal -= gift_airtime
    print(f'Hello {phone_no}, you have successfully gifted N{gift_airtime} to {rep_phone_no}, your airtime balance is N{airtime_bal}')
    start = 1
    while start == 1:
        choice = input('Are you willing to carry another transction(yes/no)? ').lower()
        if choice == 'yes':
            gifting_airtime()
            break
        elif choice == 'no':
            menu()
            break
        else:
            start = 1
            while start == 1:
                print('Please enter a correct input(yes/no)')
                choice = input('Are you willing to carry another transction(yes/no)? ').lower()
                if choice == 'yes':
                    gift_airtime()
                    break
                elif choice == 'no':
                    menu()
                    break
            start += 1
    start += 1




# Function for gifting data
def gifting_data():
    global data_bal
    print('Note: It will be deducted from your data balance')
    phone_no = input('Please enter your phone number: ')
    if len(phone_no) != 11:
        start = 1
        while start == 1:
            print('Phone number must be 11 digit')
            phone_no = input('Please enter a vaild phone number: ')
            if len(phone_no) == 11:
                break
        start += 1
    rep_phone_no = input("Please enter recipient's phone number: ")
    if len(rep_phone_no) != 11:
        start = 1
        while start == 1:
            print('Phone number must be 11 digit')
            rep_phone_no = input('Please enter a valid phone number: ')
            if len(rep_phone_no) == 11:
                break
        start += 1
    if phone_no == rep_phone_no:
        start = 1
        while start == 1:
            rep_phone_no = input("Please enter a phone number different from your's: ")
            if rep_phone_no != phone_no:
                break
        start += 1
        if len(rep_phone_no) != 11:
            start = 1
            while start == 1:
                print('Phone number must be 11 digit')
                rep_phone_no = input('Please enter a valid phone number: ')
                if len(rep_phone_no) == 11:
                    break
            start += 1
    gift_data = int(input('How much data are you gifting? '))
    if gift_data > data_bal:
        start = 1
        while start == 1:
            print(f'Sorry {name}, your data balance is {data_bal}')
            gift_data = int(input('How much data are you gifting? '))
            if gift_data <= data_bal:
                data_bal -= gift_data
                print(f'Hello {phone_no}, you have successfully gifted {gift_data}GB to {rep_phone_no}, your data balance is {data_bal}GB')
                break
        start += 1
    data_bal -= gift_data
    print(f'Hello {phone_no}, you have successfully gifted {gift_data}GB to {rep_phone_no}, your data balance is {data_bal}GB')
    start = 1
    while start == 1:
        choice = input('Are you willing to carry another transction(yes/no)? ').lower()
        if choice == 'yes':
            gifting_data()
            break
        elif choice == 'no':
            menu()
            break
        else:
            start = 1
            while start == 1:
                print('Please enter a correct input(yes/no)')
                choice = input('Are you willing to carry another transction(yes/no)? ').lower()
                if choice == 'yes':
                    gifting_data()
                    break
                elif choice == 'no':
                    menu()
                    break
            start += 1
    start += 1



# Function to exit
def exit():
    print('\n')
    response = input('Are you sure you want to exit (yes/no)? ').lower()
    if response == 'no':
        name = input('Please enter your name: ')
        code = input('Dail *123# to get started: ')
        if code == '*123#':
            menu()
        else:
            start = 1
            while start == 1:
                print(f'Sorry {name}, invalid code')
                code = input('Dail *123# to get started: ')
                if code == '*123#':
                    menu()
                    break
            start += 1
    else:
        print('Thank you for transacting with us, have a nice day')



# Main menu
def menu():
    print('\n')
    global acct_bal
    global data_bal
    global airtime_bal
    print(f'Hello {name}, welcome to Group2 app')
    print(f'Account Balance: N{acct_bal}')
    print(f'Airtime Balance: N{airtime_bal}')
    print(f'Data Balance {data_bal}GB')
    print('\n')
    print('1. To buy airtime')
    print('2. To buy data plans')
    print('3. To gift airtime')
    print('4. To gift data')
    print('5. To exit')
    ans = int(input('>>>>> '))
    if ans == 1:
        print('\n')
        acct_num = input('Please enter your account number: ')
        # Checks if the account number entered is 10 digit
        if len(acct_num) != 10:
            start = 1
            while start == 1:
                print('Account number must be 10 digit')
                acct_num = input('Please enter your account number: ')
                if len(acct_num) == 10:
                    break
            start += 1
        acct_pin = input('Please enter your 4 digit pin: ')
        # checks if the pin entered is 4 digit
        if len(acct_pin) != 4:
            start = 1
            while start == 1:
                acct_pin = input('Please enter a valid 4 digit pin: ')
                if len(acct_pin) == 4:
                    break
            start += 1
        if (len(acct_num) == 10) and (len(acct_pin) == 4):
            print('\n')
            print(f'Hello {name}, welcome to Group 2 bank')
            bank_airtime()

    elif ans == 2:
        print('\n')
        # Asking the user where he or she is purchasing data from
        choice = int(input('Where do you like to purchase from:\n1. from bank\n2. from airtime balance: '))
        # choosing to buy from bank
        if choice == 1:
            print('\n')
            acct_num = input('Please enter your account number: ')
            # Checking if the account number is 10 digit
            if len(acct_num) != 10:
                start = 1
                while start == 1:
                    print('Account number must be 10 digit')
                    acct_num = input('Please enter your account number: ')
                    if len(acct_num) == 10:
                        break
                start += 1
            acct_pin = input('Please enter your 4 digit pin: ')
            # Checking if the pin is 10 digit
            if len(acct_pin) != 4:
                start = 1
                while start == 1:
                    acct_pin = input('Please enter a valid 4 digit pin: ')
                    if len(acct_pin) == 4:
                        break
                start += 1
            if (len(acct_num) == 10) and (len(acct_pin) == 4):
                print('\n')
                print(f'Hello {name}, Welcome to group 2 bank')
                bank_data()
        # Choosing to buy from airtime balance
        elif choice == 2:
            airtime_bal_buy()
        else:
            print('Sorry cannot input')
            menu()

    elif ans == 3:
        print('\n')
        gifting_airtime()


    elif ans == 4:
        print('\n')
        gifting_data()


    elif ans == 5:
        exit()


    else:
        # telling the user to enter an option from 1 to 7
        start = 1
        while start == 1:
            print('Invalid input please select from option 1 to 5')
            ans = int(input('>>>>> '))
            if ans == 1 or ans <= 5:
                menu()
                break
        start += 1


# Beginning of the code
name = input('Please enter your name: ')
code = input('Dail *123# to get started: ')
# Checks if the code entered is correct
if code == '*123#':
    menu()
else:
    start = 1
    while start == 1:
        print(f'Sorry {name}, invalid code')
        code = input('Dail *123# to get started: ')
        if code == '*123#':
            menu()
            break
    start += 1