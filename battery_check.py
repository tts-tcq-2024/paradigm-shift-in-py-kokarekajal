from battery_limits import TEMPERATURE_LIMITS, SOC_LIMITS, CHARGE_RATE_LIMITS
from utils import is_within_range

class BatteryCheck:

    @staticmethod
    def check_temperature(temperature):
        if not is_within_range(temperature, TEMPERATURE_LIMITS):
            return False, 'temperature'
        return True, ''

    @staticmethod
    def check_soc(soc):
        if not is_within_range(soc, SOC_LIMITS):
            return False, 'state of charge (SoC)'
        return True, ''

    @staticmethod
    def check_charge_rate(charge_rate):
        if not is_within_range(charge_rate, CHARGE_RATE_LIMITS):
            return False, 'charge rate'
        return True, ''

    @staticmethod
    def battery_is_ok(temperature, soc, charge_rate):
        checks = [
            BatteryCheck.check_temperature(temperature),
            BatteryCheck.check_soc(soc),
            BatteryCheck.check_charge_rate(charge_rate)
        ]
        for check, parameter in checks:
            if not check:
                return False, f"Battery parameter {parameter} out of range!"
        return True, "Battery is ok."
