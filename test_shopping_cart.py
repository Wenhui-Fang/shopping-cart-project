from shopping_cart import to_usd
from shopping_cart import human_friendly_timestamp
import datetime

def test_to_usd():
    assert to_usd(8.88) == "$8.88"

# def test_human_friendly_timestamp(now):
#     yyyy = datetime.datetime.year
#     mm =datetime.datetime.month
#     dd = datetime.datetime.date
#     hh = datetime.datetime.hour
#     mm = datetime.datetime.minute
#     now = now()
#     assert human_friendly_timestamp(now) == yyyy+"-"+ mm + "-" + dd + " " + hh + ":" + mm