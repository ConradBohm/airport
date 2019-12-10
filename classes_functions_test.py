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

# def test_flight_add_plane():
#     test_flight = Flight()
