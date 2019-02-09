# shopping_cart.py

import datetime 
import csv


# TODO: Read from a CSV file
# C:\Users\13478\Documents\GitHub>cd shopping-cart-project

# csv_file_path = "products.csv"

# products = []

# with open(csv_file_path,"r") as f:
#     contents = csv.DictReader(f)
#     for row in contents: 
#         # print(row["name"])
#         # d = dict(row)
#         # print(d["name",d["price"]])
#         d = {"id":row["id"], "name":row["name"],"price":float(row["price"])}
#         products.append(d)


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

#Checkpoint I
#declare variables
all_user_input = []
user_input = 0
number_of_items = 0
now = datetime.datetime.now()
counter = 0
running_total = 0.0
matching_price = 0.0
selected_id = 0
tax_rate = 0.06
total_amount = 0.0
separator = "--------------------------------------"

while True:
    
    datatype_pass = True
    range_pass = True
    user_input = input("Please enter a product identifier between 1 and 20, or 'DONE' if there are no more items: ")
    if user_input == "DONE":    
        break

    #Input validation
    if not user_input.isdigit():
        print("INPUT DATA TYPE ERROR! Please only enter an integer!")
        datatype_pass = False
    if datatype_pass == True:
        if int(user_input) not in range(1,21):
            print("INPUT RANGE ERROR! Please enter an integer greater than 0 and less than 21!")
            range_pass = False
        if range_pass ==True:    
            all_user_input.append(user_input)
            number_of_items = number_of_items + 1

print("\n\nWelcome to Wen's Groceries, INC!\n")
print(separator)
print("Phone  : 347-828-4269  " + "Fax: 347-828-4268")
print("Address: 3700 O St NW, Washington DC 20057")
print("Web    : www.wensgroceries.com")
print(separator)
print("Checkout Time: " + str(now.strftime("%Y-%m-%d %H:%M:%S"))) 
print("Your shopping cart has following " + str(number_of_items)+" items: ") 
#print(*all_user_input, sep= ",")
print(separator)
print(separator + "\n")

#Checkpoint II
while counter < len(all_user_input):

    #using list apprehension to look up the item/price
    selected_id = int(all_user_input[counter])
    matching_product = [p for p in products if p["id"] == selected_id]
    product = matching_product[0]["name"]
    matching_price = matching_product[0]["price"]
    print(" + " + str(product) + " $" + str(matching_price) + "\n")
    running_total = matching_price + running_total
    counter = counter + 1

total_amount = (running_total) * ( 1 + tax_rate)
formated_running_total = "${0:.2f}".format(running_total)
formated_total_amount = "${0:.2f}".format(total_amount)
tax_amount = "${0:.2f}".format(running_total * tax_rate)

#Checkpoint III 
print(separator)
print(separator)
print("Subtotal: " + formated_running_total.rjust(25))
print("Plus D.C. Tax 6%:" + tax_amount.rjust(18))
print("Total Amout Due: " + formated_total_amount.rjust(18))
print("\nThank you for being our loyal customer. Your business is appreciated.")

