
TEMPERATURE_LIMITS = (0, 45)
SOC_LIMITS = (20, 80)
CHARGE_RATE_LIMIT = 0.8

def check_limit(value, min_limit, max_limit, vital_name):
    if value < min_limit:
        return (vital_name, 'low')
    elif value > max_limit:
        return (vital_name, 'high')
    return (vital_name, 'normal')

def check_temperature(temperature):
    return check_limit(temperature, TEMPERATURE_LIMITS[0], TEMPERATURE_LIMITS[1], 'Temperature')

def check_soc(soc):
    return check_limit(soc, SOC_LIMITS[0], SOC_LIMITS[1], 'State of Charge')

def check_charge_rate(charge_rate):
    if charge_rate > CHARGE_RATE_LIMIT:
        return ('Charge Rate', 'high')
    return ('Charge Rate', 'normal')

def battery_is_ok(temperature, soc, charge_rate):
    checks = [
        check_temperature(temperature),
        check_soc(soc),
        check_charge_rate(charge_rate)
    ]
    
    abnormal_conditions = [check for check in checks if check[1] != 'normal']
    
    if abnormal_conditions:
        for condition in abnormal_conditions:
            report_issue(condition[0], condition[1])
        return False
    
    return True

def report_issue(vital, breach_type):
    print(f'{vital} is {breach_type}!')

if __name__ == '__main__':
    assert(battery_is_ok(25, 70, 0.7) is True)
    assert(battery_is_ok(50, 85, 0.7) is False)
    assert(battery_is_ok(25, 15, 0.7) is False)
    assert(battery_is_ok(-5, 60, 0.7) is False)
    assert(battery_is_ok(25, 70, 0.85) is False)
