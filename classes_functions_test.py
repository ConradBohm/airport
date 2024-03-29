from functions import *


def test_user_creation():
    new_pass = new_passenger('Joana Thompson', 'B343123')
    assert new_pass.name == 'Joana Thompson'
    assert new_pass.passport_number == 'B343123'

    new_pass = new_passenger('Birt Kuman', 'B13927')
    assert new_pass.name == 'Birt Kuman'
    assert new_pass.passport_number == 'B13927'


def test_plane_creation():
    test_plane = Plane('0178945')
    assert test_plane.id_number == '0178945'


def test_flight_add_plane():
    test_flight = Flight()
    test_plane = Plane('0178945')

    test_flight.add_plane(test_plane.id_number)
    assert test_flight.plane == '0178945'


def test_flight_add_origin_dest():
    test_flight = Flight()
    test_flight.add_destination('Barcelona')
    assert test_flight.destination == 'Barcelona'

    test_flight.add_origin('London')
    assert test_flight.origin == 'London'


def test_flight_add_passenger():
    test_flight = Flight()
    new_pass = new_passenger('Joana Thompson', 'B343123')
    test_flight.add_passenger(new_pass)
    assert test_flight.passengers[0].name == 'Joana Thompson'
