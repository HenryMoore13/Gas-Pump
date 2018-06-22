from datetime import datetime


def get_payment():
    print('How would you like to pay today?')
    payment = input(
        '\t1 Prepay\n\t2 Pay After\n\tQ Quit\n>>> ').upper().strip()
    while not (payment == '1' or payment == '2' or payment == 'Q'):
        print('invalid')
        payment = input('>>> ').upper().strip()

    return payment


def get_gastype():
    choices = ['A', 'B', 'C']
    print('What kind of gas would you like today?')
    gas_type = input(
        '\tA Regular\n\tB Premium\n\tC Diesel\n>>> ').upper().strip()
    while not (gas_type in choices):
        print('invalid')
        gas_type = input('>>> ').upper().strip()

    if gas_type == 'A':
        return 'Regular'
    elif gas_type == 'B':
        return 'Premium'
    elif gas_type == 'C':
        return 'Diesel'

    return 'Regular'


def get_gasprice(gas_type):
    if gas_type == 'Regular':
        return 2.50
    elif gas_type == 'Premium':
        return 2.80
    if gas_type == 'Diesel':
        return 3.01


def main():
    print('welcome!')

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
