from functions import *
passenger_list = []
name_list = []
plane_list = []

print('----///---- Airport Program ----\\\\\\----\n\n')

while True:
    print('Menu:\n'
          '1 -- Add Passenger\n'
          '2 -- List Passengers\n'
          '3 -- Add Plane\n'
          '4 -- Flights\n'
          '5 -- Exit')

    choice = menu_input()

    if choice == 1:
        pass_add()

    elif choice == 2:
        for person in passenger_list:
            name_list.append(person.name)
            print(name_list)

    elif choice == 3:
        pass

    elif choice == 4:
        print('Thanks for using the program.')
        break
    else:
        print('We don\'t have that option. Try again.')


