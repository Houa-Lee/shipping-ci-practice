# tests/test_shipping.py
# pytest runs every function whose name starts with test_
from app.shipping import shipping_fee   # the code under test

def test_member_ships_free():
    # Arrange: set up the input
    total, is_member = 80, True
    # Act: call the function
    result = shipping_fee(total, is_member)
    # Assert: compare actual with expected
    assert result == 0      # True -> PASS, False -> FAIL


def test_non_member_pays_standard_fee():
    # is_member=False takes the other branch (line 4 jumps to line 6)
    assert shipping_fee(80, False) == 5.99
