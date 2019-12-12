from classes import *
from calling_SQL import *
# def new_passenger(fname, lname, number):
#     new_pass = Passenger(fname, lname, number)
#     new_pass.add_to_db()
#     cursor.execute(f'insert into passengers(first_name, last_name, passport_no) values ({names[0]}, {names[1]}, {number})')


def null_input_validation(input_str):
    if not input_str.strip():
        print('You cannot leave this field blank.')
        return False
    else:
        return True


def pass_add():
    while True:
        fname = input('Enter a first name: ')
        if not null_input_validation(fname):
            continue
        else:
            break

    while True:
        lname = input('Enter a last name: ')
        if not null_input_validation(lname):
            continue
        else:
            break

    while True:
        number = input('Enter a passport number: ')
        if not null_input_validation(number):
            continue
        else:
            break

    new_pass = Passenger(fname, lname, number)
    new_pass.add_to_db()


def list_pass():
    table_passengers.print_all()


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


