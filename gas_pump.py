from datetime import datetime


def get_payment():
    print('-----------------------------------------------------------')
    payment = input(
        '\n\t1 Prepay\n\t2 Pay After\n\tQ Quit\n>>> ').upper().strip()
    while not (payment == '1' or payment == '2' or payment == 'Q'):
        print('Invalid Choice... Please Retype Choice')
        print()
        payment = input('>>> ').upper().strip()

    return payment


def get_gastype():
    choices = 'REGULAR PLUS PREMIUM'.split()
    print('-----------------------------------------------------------')
    print('(Regular)', '(Plus)', '(Premium)')
    gas_type = input('\nWhat Type Of Gas Would You Like? ').upper().strip()
    while not (gas_type in choices):
        print('invalid')
        gas_type = input('>>> ').upper().strip()
    return gas_type


def get_gasprice(gas_type):
    if gas_type == 'REGULAR':
        return 2.50
    elif gas_type == 'PLUS':
        return 2.80
    elif gas_type == 'PREMIUM':
        return 3.01


def main():
    print('\nWelcome to Gas-Mart!!!\n')
    name = input('What is your name? ')
    print('\nHello', name)
    payment = get_payment()
    if payment == 'Q':
        print('thank you come again')
        exit()

    gas_type = get_gastype()
    price = get_gasprice(gas_type)

    print('payment', payment)
    print('type', gas_type)
    print('price', price)


if __name__ == '__main__':
    main()
