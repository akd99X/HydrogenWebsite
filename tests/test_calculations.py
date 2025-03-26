# tests/test_calculations.py
from src.app import calculate_power


def test_power_calculation():
    # Test valid input
    assert calculate_power(1000) == 33.33  # 1000g → 33.33 kW

    assert calculate_power(500) == 16.67  # 500g → 16.67 kW


    # Test invalid input (e.g., negative values)
    try:
        calculate_power(-100)
        assert False  # Should raise an error
    except ValueError:
        assert True
