from functions import *

# passenger_list = []
name_list = []
plane_list = []
flight_list = []
i_d = 1

print('----///---- Airport Program ----\\\\\\----\n\n')

while True:
    print('Menu:\n'
          '1 -- Add Passenger\n'
          '2 -- List Passengers\n'
          '3 -- Add Plane\n'
          '4 -- Flight List\n'
          '5 -- Exit')

    choice = menu_input()

    if choice == 1:
        pass_add()

    elif choice == 2:
        list_pass()


    elif choice == 3:
        plane_add(plane_list)

    elif choice == 4:
        while True:
            print('Menu:\n'
                  '1 -- Create Flight\n'
                  '2 -- Add Destination\n'
                  '3 -- Add Origin\n'
                  '4 -- Add Passenger\n'
                  '5 -- Flight details\n'
                  '6 -- Exit')
            choice = menu_input()

            if choice == 1:
                new_flight = Flight(i_d)
                flight_list.append(new_flight)

                i_d += 1

            elif choice == 2:
                num = (input('id '))
                dest = input('Destination: ')
                for flight in flight_list:
                    if flight.id == num:
                        flight.destination = dest
                        break

            elif choice == 3:
                num = (input('id '))
                orig = input('Origin: ')
                for flight in flight_list:
                    if flight.id == num:
                        flight.origin = orig
                        break

            elif choice == 4:
                num = (input('id '))
                name = input('Passenger: ')
                for flight in flight_list:
                    if flight.id == num:
                        for person in passenger_list:
                            if name in person.name:
                                flight.add_passenger(person)
                                break
                        break

            elif choice == 5:
                num = input('id ')
                for flight in flight_list:
                    if flight.id == num:
                        print(f'Flight id: {flight.id}'
                              f'Flight Destination: {flight.destination}'
                              f'Flight Origin: {flight.origin}')
                        break
            elif choice == 6:
                break
            else:
                print('We don\'t have that option. Try again.')

    elif choice == 5:
        print('Thanks for using the program.')
        break
    else:
        print('We don\'t have that option. Try again.')


