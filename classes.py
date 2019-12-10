class Passenger:
    def __init__(self, name, pass_num):
        self.name = name
        self.passport_number = pass_num


class Plane:
    def __init__(self, number):
        self.id_number = number


class Flight:
    def __init__(self):
        self.plane = ''
        self.destination = ''
        self.origin = ''
        self.passengers = []

    def add_plane(self, plane):
        pass

    def add_destination(self, dest):
        self.destination = dest

    def add_origin(self, origin):
        self.origin = origin

    def add_passenger(self, passenger):
        self.passengers.append(passenger)