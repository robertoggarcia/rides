from app.drivers import activate_driver
from app.rides import new_ride, finish_ride
from utils.schemas import driver_schema, ride_schema


def test_ride_schema():
    driver = {'ride': {'...': '...'}, 'driver': 'driver-1'}

    assert ride_schema(driver), 'Should be a ride schema'


def test_new_ride():
    drivers = {}
    driver = {'driver': 'driver-1', 'name': 'Robert', 'car': 'Aveo'}
    drivers = activate_driver(driver, drivers)
    new_ride_data = {'ride': {}, 'driver': 'driver-1'}
    drivers = new_ride(new_ride_data, drivers)

    assert drivers['driver-1']['onRide'], 'The driver it not on ride'


def test_ride_driver_ban():
    drivers = {}
    driver = {'driver': 'driver-1', 'name': 'Robert', 'car': 'Aveo'}
    drivers = activate_driver(driver, drivers)
    drivers['driver-1']['status'] = 'banned'

    new_ride_data = {'ride': {}, 'driver': 'driver-1'}
    drivers = new_ride(new_ride_data, drivers)

    assert drivers['driver-1']['violations'][0] == 'driver-banned', 'The driver already exists'


def test_finish_ride():
    drivers = {}
    rides = {}
    driver = {'driver': 'driver-1', 'name': 'Robert', 'car': 'Aveo'}
    drivers = activate_driver(driver, drivers)
    new_ride_data = {'ride': {'id': 'ride-1', 'user': 'user-1', 'estimatedKm': 12, 'estimatedMinutes': 10,
                     'estimatedPrice': 45, 'status': 'start'}, 'driver': 'driver-1'}
    drivers = new_ride(new_ride_data, drivers)
    rides['ride-1'] = new_ride_data['ride']

    ride = {'ride': {'id': 'ride-1', 'user': 'user-1', 'estimatedKm': 12, 'estimatedMinutes': 10,
                     'estimatedPrice': 45, 'status': 'finished', 'km': 12, 'minutes': 10, 'price': 30},
            'driver': 'driver-1'}
    rides, drivers = finish_ride(ride, rides, drivers)

    assert 'ride-1' in rides
    assert not drivers['driver-1']['onRide'], 'The driver is not finish the ride'


def test_finish_ride_not_start():
    drivers = {}
    rides = {}
    driver = {'driver': 'driver-1', 'name': 'Robert', 'car': 'Aveo'}
    drivers = activate_driver(driver, drivers)
    new_ride_data = {'ride': {'id': 'ride-1', 'user': 'user-1', 'estimatedKm': 12, 'estimatedMinutes': 10,
                     'estimatedPrice': 45, 'status': 'start'}, 'driver': 'driver-1'}
    drivers = new_ride(new_ride_data, drivers)

    ride = {'ride': {'id': 'ride-2', 'user': 'user-1', 'estimatedKm': 12, 'estimatedMinutes': 10,
                     'estimatedPrice': 45, 'status': 'finished', 'km': 12, 'minutes': 10, 'price': 30},
            'driver': 'driver-1'}
    rides, drivers = finish_ride(ride, rides, drivers)

    assert drivers['driver-1']['violations'][0] == 'ride-was-never-started', 'The ride was already started'
