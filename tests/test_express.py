# tests/test_express.py
from app.shipping import express_fee

def test_far_away_costs_25():
    # distance > 50 km -> first if is True
    assert express_fee(40, 80) == 25.00

def test_big_order_nearby_costs_10():
    # close by, total >= 100 -> second if is True
    assert express_fee(120, 10) == 10.00

def test_small_order_nearby_costs_15():
    # close by, total < 100 -> both ifs are False
    assert express_fee(40, 10) == 15.00
