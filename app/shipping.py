def shipping_fee(total, is_member):
    """Return the shipping fee in dollars."""
    fee = 5.99          # everyone starts at $5.99
    if is_member:       # DECISION: True or False?
        fee = 0         # members ship free
    return fee          # send the fee back


def express_fee(total, distance_km):
    """Return the express-delivery fee in dollars."""
    if distance_km > 50:     # far away costs more
        return 25.00
    if total >= 100:         # big orders get a discount
        return 10.00
    return 15.00             # everyone else
