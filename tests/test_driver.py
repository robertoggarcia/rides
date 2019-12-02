from app.drivers import activate_driver, ban_driver
from utils.schemas import driver_schema


def test_driver_schema():
    driver = {'driver': 'driver-1', 'name': 'Robert', 'car': 'Aveo'}
    assert driver_schema(driver), 'Should be a driver'


def test_activate_driver():
    driver = {'driver': 'driver-1', 'name': 'Robert', 'car': 'Aveo'}
    drivers = {}
    drivers = activate_driver(driver, drivers)

    assert drivers['driver-1']['status'] == 'activated', 'It is not an active driver'


def test_drive_violations():
    driver = {'driver': 'driver-1', 'name': 'Robert', 'car': 'Aveo'}
    drivers = {}
    drivers = activate_driver(driver, drivers)

    driver_2 = {'driver': 'driver-1', 'name': 'Robert', 'car': 'Aveo'}
    drivers = activate_driver(driver_2, drivers)

    assert drivers['driver-1']['violations'][0] == 'driver-already-created', 'The driver already exists'


def test_ban_driver():
    driver = {'driver': 'driver-1', 'name': 'Robert', 'car': 'Aveo'}
    drivers = {}
    drivers = activate_driver(driver, drivers)
    drivers = ban_driver(driver, drivers)

    assert drivers['driver-1']['status'] == 'banned'


def test_ban_driver_banned():
    driver = {'driver': 'driver-1', 'name': 'Robert', 'car': 'Aveo'}
    drivers = {}
    drivers = activate_driver(driver, drivers)
    drivers = ban_driver(driver, drivers)
    drivers = ban_driver(driver, drivers)

    assert drivers['driver-1']['violations'][0] == 'driver-already-banned'


def test_ban_driver_on_ride():
    driver = {'driver': 'driver-1', 'name': 'Robert', 'car': 'Aveo'}
    drivers = {}
    drivers = activate_driver(driver, drivers)
    drivers['driver-1']['onRide'] = True
    drivers = ban_driver(driver, drivers)

    assert drivers['driver-1']['violations'][0] == 'driver-on-ride'
