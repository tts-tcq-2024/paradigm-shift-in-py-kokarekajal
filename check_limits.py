# main.py

from battery_check import BatteryCheck

def run_tests():
    assert BatteryCheck.battery_is_ok(25, 70, 0.7) == (True, "Battery is ok.")
    assert BatteryCheck.battery_is_ok(50, 70, 0.7) == (False, "Battery parameter temperature out of range!")
    assert BatteryCheck.battery_is_ok(25, 85, 0.7) == (False, "Battery parameter state of charge (SoC) out of range!")
    assert BatteryCheck.battery_is_ok(25, 70, 0.9) == (False, "Battery parameter charge rate out of range!")

    assert BatteryCheck.battery_is_ok(0, 70, 0.7) == (True, "Battery is ok.")
    assert BatteryCheck.battery_is_ok(45, 70, 0.7) == (True, "Battery is ok.")
    assert BatteryCheck.battery_is_ok(-1, 70, 0.7) == (False, "Battery parameter temperature out of range!")
    assert BatteryCheck.battery_is_ok(46, 70, 0.7) == (False, "Battery parameter temperature out of range!")

    assert BatteryCheck.battery_is_ok(25, 20, 0.7) == (True, "Battery is ok.")
    assert BatteryCheck.battery_is_ok(25, 80, 0.7) == (True, "Battery is ok.")
    assert BatteryCheck.battery_is_ok(25, 19, 0.7) == (False, "Battery parameter state of charge (SoC) out of range!")
    assert BatteryCheck.battery_is_ok(25, 81, 0.7) == (False, "Battery parameter state of charge (SoC) out of range!")

    assert BatteryCheck.battery_is_ok(25, 70, 0) == (True, "Battery is ok.")
    assert BatteryCheck.battery_is_ok(25, 70, 0.8) == (True, "Battery is ok.")
    assert BatteryCheck.battery_is_ok(25, 70, 0.9) == (False, "Battery parameter charge rate out of range!")

    print("All tests passed!")

if __name__ == '__main__':
    run_tests()
