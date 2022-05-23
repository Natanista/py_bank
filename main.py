accountName = ""
accountId = ""
balance = 0
previousTransaction = 0


def main(acName, acId):
    accountName = acName
    accountId = acId
    showMenu()


def deposit(amount):
    global balance, previousTransaction
    balance += amount
    previousTransaction = amount


def withdraw(amount):
    global balance, previousTransaction
    balance = balance - amount
    previousTransaction = -amount
    
def getPreviousTransaction():
    if previousTransaction > 0:
        print('You deposit: ', previousTransaction)
    elif previousTransaction < 0:
        print('You withdraw: ', previousTransaction)
    else:
        print('There is no transaction')

def showMenu():
    print('--------------------------------------')
    print('WELCOME TO PY BANK')
    print('--------------------------------------')
    print('1. Check Balance')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. Previous Transaction')
    print('5. Exit')
    print('--------------------------------------')
    option = ''
    amount = 0

    while option != '5':
        option = input('Select an option:')
        if option == '1':
            print('Your balance is: ', balance)
        elif option == '2':
            try:
                amount = int(input('Enter amount of deposit:'))
                deposit(amount)
            except ValueError:
                print('Not a valid number!')
        elif option == '3':
            try:
                amount = int(input('Enter amount of withdraw:'))
                withdraw(amount)
            except ValueError:
                print('Not a valid number!')
        elif option == '4':
            getPreviousTransaction()
        elif option == '5':
            print
            '************************************'
        else:
            print
            'Option invalid! Please try again!'

    print('Thank you for using our service!')


main("Natan", "001")


