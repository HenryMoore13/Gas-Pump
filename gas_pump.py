from datetime import datetime


def get_payment():
    print('-----------------------------------------------------------')
    payment = input(
        '\n\t1 Prepay\n\t2 Pay After\n\tQ Quit\n>>> ').upper().strip()
    while not (payment == '1' or payment == '2' or payment == 'Q'):
        print('Invalid Choice... Please Retype Choice')
        print()
        payment = input('>>> ').upper().strip()

    if payment == '1':
        return 'PREPAY'
    elif payment == '2':
        return 'PAY AFTER'
    return payment


def get_gastype():
    choices = 'REGULAR PLUS PREMIUM'.split()
    print('-----------------------------------------------------------')
    print('(Regular)', '(Plus)', '(Premium)')
    gas_type = input('\nWhat Type Of Gas Would You Like? ').upper().strip()
    while not (gas_type in choices):
        print('Invalid Choice... Please Retype Choice')
        gas_type = input('>>> ').upper().strip()

    print(gas_type, 'SELECTED')
    return gas_type


def get_gasprice(gas_type):
    if gas_type == 'REGULAR':
        price = 2.50
    elif gas_type == 'PLUS':
        price = 2.80
    elif gas_type == 'PREMIUM':
        price = 3.01
    else:
        price = 0

    print('${:.2f} per gal'.format(price))
    return price


def get_gallons():
    print('-----------------------------------------------------------')
    gallons = input('\nHow Many gallons Are You Buying? ').strip()
    while not (gallons.isdigit()):
        print('Invalid Choice... Please Retype Choice')
        gallons = input('>>> ')
    return int(gallons)


def get_dollars():
    print('-----------------------------------------------------------')
    dollars = input('\nHow Much Money are you Spending? ').strip()
    while not (dollars.isdigit()):
        print('Invalid Choice... Please Retype Choice')
        dollars = input('>>> ')
    return int(dollars)


def get_gallons_prepay(price, money):
    return money / price


def get_money_pay_after(price, gallons):
    return price * gallons


def write_to_history(payment, gas_type, price, gallons, money):
    time = datetime.now()
    text = '\n{}, {}, {}, {:.3f}, {:.2f}'.format(time, payment, gas_type,
                                                 price, gallons, money)
    with open('history.txt', 'a') as file:
        file.write(text)


def main():
    print('\nWelcome to Gas-Mart!!!\n')
    name = input('What is your name? ')
    print('\nHello', name)
    payment = get_payment()
    if payment == 'Q':
        print('Thank you come again!!')
        exit()

    gas_type = get_gastype()
    price = get_gasprice(gas_type)

    if payment == 'PAY AFTER':
        gallons = get_gallons()
        money = get_money_pay_after(price, gallons)
    elif payment == 'PREPAY':
        money = get_dollars()
        gallons = get_gallons_prepay(price, money)

    print('Payment Method', payment)
    print('-----------------------------------------------------------')
    print('Fuel Type', gas_type)
    print('\t${:.2f} per gal'.format(price))
    print('Gallons', round(gallons, 3))
    print('TOTAL:', '${:.2f}'.format(money))

    write_to_history(payment, gas_type, price, gallons, money)


if __name__ == '__main__':
    main()
