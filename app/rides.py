def new_ride(obj, drivers):
    """
    Update driver status on ride (and violations in case).
    """
    if obj['driver'] in drivers:
        driver = drivers[obj['driver']]
        if driver['status'] != 'activated':
            violations = driver.get('violations', [])
            violations.append('driver-banned')
            driver['violations'] = violations
            return drivers
        if driver['onRide']:
            violations = driver.get('violations', [])
            violations.append('driver-on-ride')
            driver['violations'] = violations
            return drivers
        driver['onRide'] = True
    return drivers


def finish_ride(obj, rides, drivers):
    if obj['ride']['id'] not in rides:
        driver = drivers[obj['driver']]
        violations = driver.get('violations', [])
        violations.append('ride-was-never-started')
        driver['violations'] = violations
        return rides, drivers
    drivers[obj['driver']]['onRide'] = False
    rides[obj['ride']['id']] = obj['ride']
    return rides, drivers
