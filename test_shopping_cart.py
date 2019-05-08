from shopping_cart import to_usd
from shopping_cart import human_friendly_timestamp
from shopping_cart import find_product
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

def test_find_product():
    products = [
        {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
        {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
        {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
        {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
        {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    ]
    matching_product = find_product("3", products)
    assert matching_product["name"] == "Robust Golden Unsweetened Oolong Tea"