def show_balance():
    print(f'Your balance is {balance:.2f} Rupees')
def deposit():
    amount = float(input('Enter your Amount to deposit:'))
    
    if amount < 0:
        print('This is an invalid amount')
        return 0
    else:
        return amount
    
def withdrawal():
    amount = float(input('Enter the amount to withdraw:'))

    if amount > balance:
        print('Insufficient Balance')
        return 0
    elif amount < 0 :
        print('Amount must be greater than Zero')
        return 0
    else:
        return amount
balance = 0
is_running = True

while is_running:
    print('******************')
    print('Banking Programme')
    print('******************')
    print('1. Show_balance')
    print('2. Deposit')
    print('3. Withdrawal')
    print('4. Exit')

    choice = int(input('Enter your Choice (1-4):'))
    if choice == 1 :
        show_balance()
    elif choice == 2:
        balance += deposit()
    elif choice == 3:
        balance -= withdrawal()
    elif choice == 4:
        is_running = False
    else:
        print('it is an invalid choice')

print('**************************')
print('Thank You! Have a nice day')
print('***************************')
    
