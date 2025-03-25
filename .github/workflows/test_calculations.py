# tests/test_calculations.py
from app import calculate_power

def test_power_calculation():
    # Test valid input
    assert calculate_power(1000) == 33.3  # 1000g → 33.3 kW
    assert calculate_power(500) == 16.65  # 500g → 16.65 kW

    # Test invalid input (e.g., negative values)
    try:
        calculate_power(-100)
        assert False  # Should raise an error
    except ValueError:
        assert True
