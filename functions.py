from classes import *


def new_passenger(name, number):
    new_pass = Passenger(name, number)
    return new_pass


def null_input_validation(input_str):
    if not input_str.strip():
        print('You cannot leave this field blank.')
        return False
    else:
        return True


def pass_add(passenger_list):
    while True:
        name = input('Enter a name: ')
        if not null_input_validation(name):
            continue
        else:
            break

    while True:
        number = input('Enter a passport number: ')
        if not null_input_validation(number):
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


def plane_add(plane_list):
    while True:
        number = input('Input plane number to be added: ')
        if not null_input_validation(number):
            print('Please enter in this field')
        else:
            break

        new_plane = Plane(number)
        plane_list.append(new_plane)
        print('New plane added.')
