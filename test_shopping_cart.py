from shopping_cart import to_usd
from shopping_cart import human_friendly_timestamp
from shopping_cart import find_product
import datetime

def test_to_usd():
    assert to_usd(8.88) == "$8.88"

#very stupid test method - needs revision
def test_human_friendly_timestamp():
    string_time = str(datetime.datetime.now())
    now = datetime.datetime.now()
    assert human_friendly_timestamp(now) == string_time[0] + string_time[1] + string_time[2] + string_time[3] +  \
        string_time[4] + string_time[5] + string_time[6] + string_time[7] + string_time[8] + string_time[9] + string_time[10] + \
        string_time[11] + string_time[12] + string_time[13] + string_time[14] + string_time[15] + string_time[16] + string_time[17]  + string_time[18]
            
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