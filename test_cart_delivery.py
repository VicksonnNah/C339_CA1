import pytest
from cart_delivery import qualifies_free_delivery

# Valid & Boundary Cases (Boundary at 5000 cents)
@pytest.mark.parametrize("total, expected", [
    (0, False),           # Lower boundary
    (4999, False),        # Just below threshold
    (5000, True),         # Exact threshold (Expected to FAIL due to > 5000 bug)
    (5001, True),         # Just above threshold
    (10000, True),        # Well above threshold
])
def test_qualifies_free_delivery_isvalid(total, expected):
    assert qualifies_free_delivery(total) is expected

# Invalid Data Types raises TypeError
@pytest.mark.parametrize("invalid_input", [
    "5000",
    50.00,
    True,                 
    False,
    None,
])
def test_qualifies_free_delivery_raises_type_error(invalid_input):
    with pytest.raises(TypeError):
        qualifies_free_delivery(invalid_input)

# Out-of-Range Values raises ValueError
@pytest.mark.parametrize("negative_total", [-1, -5000])
def test_qualifies_free_delivery_gives_value_error(negative_total):
    with pytest.raises(ValueError):
        qualifies_free_delivery(negative_total)
