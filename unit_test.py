import pytest

# Assuming the provided code is in a file named `app.py`
# We need to test the calculation logic, not the UI.
# So we'll simulate the calculations.

# To test the logic, we'd typically refactor the core calculation
# into a separate function. For this simple case, we can write a test
# that checks the output for a known input.

def calculate_powers(n):
    """
    Calculates the square, cube, and fifth power of a number.
    This function isolates the core logic from the Streamlit UI.
    """
    square = n ** 2
    cube = n ** 3
    fifth_power = n ** 5
    return square, cube, fifth_power

# Create a fixture to hold test data
@pytest.mark.parametrize("input_number, expected_square, expected_cube, expected_fifth", [
    (2, 4, 8, 32),
    (3, 9, 27, 243),
    (0, 0, 0, 0),
    (1, 1, 1, 1),
    (-2, 4, -8, -32),
])
def test_power_calculations(input_number, expected_square, expected_cube, expected_fifth):
    """
    Tests if the power calculations are correct for various inputs.
    """
    square, cube, fifth_power = calculate_powers(input_number)
    
    # Assert that the calculated values match the expected values
    assert square == expected_square
    assert cube == expected_cube
    assert fifth_power == expected_fifth