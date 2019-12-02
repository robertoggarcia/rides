def driver_schema(obj):
    return 'driver' in obj and 'name' in obj and 'car' in obj


def ride_schema(obj):
    return 'ride' in obj and 'driver' in obj and 'km' not in obj['ride'] and 'price' not in obj['ride']


def ban_schema(obj):
    return 'ban' in obj and 'driver' in obj


def finish_ride_schema(obj):
    return 'ride' in obj and 'driver' in obj and 'km' in obj['ride'] and 'price' in obj['ride']
