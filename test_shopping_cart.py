from shopping_cart import to_usd
from shopping_cart import human_friendly_timestamp
import datetime

def test_to_usd():
    assert to_usd(8.88) == "$8.88"

# def test_human_friendly_timestamp():
#     datetime.datetime.now()
#     yyyy = datetime.date.today().year
#     mm = datetime.date.today().month
#     dd = datetime.date.today().date
#     hm = datetime.datetime.strftime('%H:%M')
#     breakpoint()
#     assert human_friendly_timestamp(now) == str(yyyy) +"-"+ str(mm) + "-" + str(dd) + " " + str(hh) + ":" + str(mm)