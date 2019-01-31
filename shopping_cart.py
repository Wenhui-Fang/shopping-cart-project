# shopping_cart.py

import datetime 

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

# TODO: write some Python code here to produce the desired functionality...

# print(products)

# user_input = input("Please enter an identifier number, or DONE if you finish.")

# print(input)

all_user_input = []
user_input = 0
number_of_items = 0
# user_input = input("Please input a product identifier, or 'DONE' if there are no more items: ")
# print("YOUR INPUT WAS: " + user_input)
# all_user_input.append(user_input)

# an infinite loop! you can press control+c to cancel the program if/when it gets stuck...
while user_input != "DONE":

    # capturing user input and storing in a variable
    # demonstrating ability to recognize what the input was, although you might also want to check its datatype
    user_input = input("Please input a product identifier, or 'DONE' if there are no more items: ")
    print("YOUR INPUT WAS: " + user_input)
    
    if user_input == "DONE":
        break
    
    all_user_input.append(user_input)
    number_of_items = number_of_items + 1

print("Your shopping cart currently has the following " + str(number_of_items) + " items: ")
print(*all_user_input, sep= ",")



# now = datetime.datetime.now()

# print(now)

# print("First element: ")
# print(all_user_input[0])

counter = 0

running_total = 0

price = 0

selected_id = 0

#all_user_input[0]

while counter < len(all_user_input):

    # print(all_user_input[2])

    selected_id = int(all_user_input[counter])
    # print("The selected ID is: ")    
    # print(selected_id)

    product = products[selected_id]["name"]

    price = products[selected_id]["price"]
 
    print(" + " + str(product) + " $" + str(price))

    running_total = price + running_total

    counter = counter + 1

print("The total amount is: ")
print(" $" + str(running_total))


    # selected_id = 1

    # matching_product = [p for p in products if p["id"] == selected_id]

    # product = matching_product[0]
    # print(product)

    # price = product["price"]

    # print("The matching product is: ") 

    # print(selected_id)
    
    # counter = counter + 1
    # print("The selected ID is: ")
    # print(selected_id)

    # matching_product = [p for p in products if p["id"] == selected_id]

    # matching_product = [p for p in products if p["id"] == selected_id]

    # print(matching_product)

    # print(matching_product[0]["price"])
    # price = matching_product[0]["price"]

    # price = running_total + price
    # counter = counter + 1

    # print(price)

#     product = matching_product["name"]

#     print(product)

#     price = product["price"]

#     price = running_total + price
      
# print(price)

# calculate tax, add tax + total 



