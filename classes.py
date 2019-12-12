from calling_SQL import *


class Passenger(AirportConnection):
    def __init__(self, fname, lname, pass_num):
        super().__init__()
        self.first_name = fname
        self.last_name = lname
        self.passport_number = pass_num

    def add_to_db(self):
        query = f"insert into passengers(first_name, last_name, passport_no) values ('{self.first_name}', " \
                f"'{self.last_name}', '{self.passport_number}')"

        self.cursor.execute(query)
        self.docker_airport.commit()

    def print_all(self):
        query = 'select * from passengers'
        data = self.cursor.execute(query)
        while True:
            record = data.fetchone()
            if record is None:
                break
            print(record)

class Plane(AirportConnection):
    def __init__(self, number):
        super().__init__()
        self.id_number = number


class Flight(AirportConnection):
    def __init__(self, i_d):
        super().__init__()
        self.plane = ''
        self.destination = ''
        self.origin = ''
        self.passengers = []
        self.id = i_d

    def add_plane(self, plane):
        self.plane = plane

    def add_destination(self, dest):
        self.destination = dest

    def add_origin(self, origin):
        self.origin = origin

    def add_passenger(self, passenger):
        self.passengers.append(passenger)


table_passengers = Passenger('table', 'table', '0')
table_flights = Flight(0)
table_planes = Plane(0)
