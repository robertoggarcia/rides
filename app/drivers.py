def activate_driver(obj, drivers):
    """
    Create or update driver and violations.
    """
    driver = obj['driver']
    if driver in drivers:
        violations = drivers[driver].get('violations', [])
        violations.append('driver-already-created')
        drivers[driver]['violations'] = violations
        return drivers
    drivers[driver] = obj
    drivers[driver]['status'] = 'activated'
    drivers[driver]['onRide'] = False
    drivers[driver]['violations'] = []
    return drivers


def ban_driver(obj, drivers):
    """
    Ban a driver (update violations in case).
    """
    if obj['driver'] in drivers:
        driver = drivers[obj['driver']]
        if driver['status'] != 'activated':
            violations = driver.get('violations', [])
            violations.append('driver-already-banned')
            driver['violations'] = violations
            return drivers
        if driver['onRide']:
            violations = driver.get('violations', [])
            violations.append('driver-on-ride')
            driver['violations'] = violations
            return drivers
        driver['status'] = 'banned'
        driver['violations'] = driver.get('violations', [])
    return drivers
