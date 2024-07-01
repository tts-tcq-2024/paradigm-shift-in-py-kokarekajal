
def is_temperature_out_of_range(temperature):
    return temperature < 0 or temperature > 45
def is_soc_out_of_range(soc):
    return soc < 20 or soc > 80
def is_charge_rate_out_of_range(charge_rate):
    return charge_rate > 0.8
def battery_is_ok(temperature, soc, charge_rate):
    return not (is_temperature_out_of_range(temperature) or is_soc_out_of_range(soc) or is_charge_rate_out_of_range(charge_rate))
if __name__ == '__main__':
    assert battery_is_ok(25, 70, 0.7) is True
    assert battery_is_ok(50, 85, 0) is False
