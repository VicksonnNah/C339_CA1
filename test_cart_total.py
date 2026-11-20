import pytest
from cart_total import calculate_total

# Valid & Boundary Cases
@pytest.mark.parametrize("price, qty, expected", [
    (1000, 3, 3000),      # Standard positive values
    (0, 5, 0),            # Boundary: zero unit price
    (1000, 0, 0),         # Boundary: zero quantity (Expected to FAIL due to bug)
    (0, 0, 0),            # Boundary: both zero
])
def test_calculate_total_isvalid(price, qty, expected):
    assert calculate_total(price, qty) == expected

# Invalid Data Types -> TypeError
@pytest.mark.parametrize("price, qty", [
    ("1000", 2),
    (1000, "2"),
    (10.50, 2),
    (True, 2),            # Boolean check per General Requirement 2
    (1000, False),
    (None, 1),
])
def test_calculate_total_type_error(price, qty):
    with pytest.raises(TypeError):
        calculate_total(price, qty)

# Out-of-Range Values -> ValueError
@pytest.mark.parametrize("price, qty", [
    (-1, 2),
    (1000, -1),
    (-100, -5),
])
def test_calculate_total_value_error(price, qty):
    with pytest.raises(ValueError):
        calculate_total(price, qty)