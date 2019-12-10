from classes import *


def new_passenger(name, number):
    new_pass = Passenger(name, number)
    return new_pass


def new_pass_input_validation(input_str):
    if not input_str.strip():
        print('You cannot leave this field blank.')
        return False
    else:
        return True


def pass_add():
    while True:
        name = input('Enter a name: ')
        if not new_pass_input_validation(name):
            continue
        else:
            break

    while True:
        number = input('Enter a passport number: ')
        if not new_pass_input_validation(number):
            continue
        else:
            break

    new_pass = new_passenger(name, number)
    passenger_list.append(new_pass)


def menu_input():
    while True:
        try:
            choice = int(input('Pick a number from the menu options: '))
            break
        except ValueError:
            print('\nNot a valid number, try again with a number digit from the menu.')

    return choice



