import json

from .drivers import activate_driver, ban_driver
from .rides import new_ride, finish_ride
from utils.schemas import driver_schema, ride_schema, ban_schema, finish_ride_schema

operations = open('data/operations.json')
drivers = {}
rides = {}

for opt in operations:
    opt_json = json.loads(opt)

    if driver_schema(opt_json):
        drivers = activate_driver(opt_json, drivers)

    if ride_schema(opt_json):
        drivers = new_ride(opt_json, drivers)
        ride = opt_json['ride']
        rides[ride['id']] = ride

    if ban_schema(opt_json):
        drivers = ban_driver(opt_json, drivers)

    if finish_ride_schema(opt_json):
        rides, drivers = finish_ride(opt_json, rides, drivers)

print(json.dumps(drivers, indent=4))
