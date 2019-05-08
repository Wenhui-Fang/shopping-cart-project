from shopping_cart import to_usd
from shopping_cart import human_friendly_timestamp

def test_to_usd():
    assert to_usd(8.88) == "$8.88"

# def test_human_friendly_timestamp():
#     assert human_friendly_timestamp(now) = 