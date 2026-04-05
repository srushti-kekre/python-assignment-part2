import copy


menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}


#Task 1 — Explore the Menu 
#Print the full menu grouped by category, formatted like:

# We first get the categories
categories = []
for key,val in menu.items():
    #print(val)
    categories.append(val['category'])

#removing duplicates by converting to set and then back again to list
categories = set(categories)
categories = list(categories)
#print(categories)

#Start printing
for category in categories:
    print(f"{'='*10} {category}{'='*10}")
    for key,val in menu.items():
        if(val["category"] == category):
            if(val["available"]):
                availablity_string = "[Available]"
            else:
                availablity_string = "[Not Available]"
            #print(f"{key}   {val["price"]}  {availablity_string}")
            print(f"{key}   {val['price']}  {availablity_string}")
    print(f"\n")

"""
Using dictionary methods, compute and print:

Total number of items on the menu
Total number of available items
The most expensive item (name + price)
All items priced under ₹150 (name + price)
"""

total_items = len(menu)

count_available = 0
for key,val in menu.items():
    if(val["available"]):
        count_available +=1

most_expensive_item_price = 0
most_expensive_item = ""
for key,val in menu.items():
    if(val["price"] >  most_expensive_item_price):
        most_expensive_item_price = val["price"]
        most_expensive_item = val["category"]

items_above_150 = {}
for key,val in menu.items():
    if(val["price"]>150):
        items_above_150[key] = val["price"]


print(f"Total available menu items are {total_items}")
print(f"Total available menu items are {count_available}")
print(f"Most expensive item is {most_expensive_item} with price {most_expensive_item_price}")
print(f"Items above 150₹")
for key,val in items_above_150.items():
    print(f"Item - {key}, price - {val}")   

############################################################################################
#Task 2 — Cart Operations (8 marks)
cart = []
#Each cart entry should look like: {"item": "Paneer Tikka", "quantity": 2, "price": 180.0}

#
def add_item(menu_item,qty=1):
    if menu_item not in menu:
        print(f"{menu_item} to be added is not in Menu, please recheck")
        return -1
        #TODO- can show available menu list
    #if code comes till this pt, we have menu_item in menu
    if(menu[menu_item]["available"] == True):
        for item_dict in cart:
            if(item_dict["item"] == menu_item):
                item_dict["quantity"] = item_dict["quantity"] + qty
                break
        else:
            val = menu[menu_item]
            #Time to add the item in our dictionary
            cart.append({"item":menu_item,"quantity":qty,"price":val["price"]})
        return 1
    else:
        print(f"{menu_item} is not available currently")
        return 1


def remove_item(menu_item,qty=1):
    if menu_item not in menu:
        print(f"{menu_item} to be added is not in Menu, please recheck")
        return -1
        #TODO- can show available menu list
    for item_dict in cart:
        if(item_dict["item"] == menu_item):
            item_dict["quantity"] = item_dict["quantity"] - qty
            if(item_dict["quantity"] <= 0):
                cart.remove(item_dict)
            break
    else:
        print(f"{menu_item} is not in cart")
    pass
def update_qty():
    pass

#Testing 
print(f"Initial Cart is {cart}")
add_item("Paneer Tikka",2)
add_item("Gulab Jamun",7)
add_item("Paneer Tikka")
add_item("Chicken Wings")
add_item("Mystery Burger")
remove_item("Gulab Jamun")
print(f"Final Cart is {cart}")

#Write logic to update the quantity of an item already in the cart. - Already covered in ADD ITEM. You can update qty via that
    
order_summary = {"updated_cart":cart,"subtotal":0,"gst":5,"total":0}

subtotal = 0
for cart_item in order_summary["updated_cart"]:
    total = cart_item["quantity"] * cart_item["price"]
    cart_item["total"] = total

    subtotal = subtotal + total

total = subtotal + (subtotal * order_summary['gst'])
order_summary["subtotal"] = subtotal
order_summary["total"] = total

#print(order_summary)  

#5.Print a final Order Summary:
print(f"{'='*10}  Order Summary {'='*10} ")
for cart_item in order_summary["updated_cart"]:
    print(f"{cart_item['item']} \t{cart_item['quantity']}\t{cart_item['total']}")
print(f"{'-'*36}")
print(f"subtotal \t\t {order_summary["subtotal"]}")

print(f"gst \t\t\t {order_summary["gst"]}%")

print(f"Total \t\t\t {order_summary["total"]}")
print(f"{'='*36}")


############################################################################################
#Task 3 

#3.1.Deep copy inventory into a variable called inventory_backup before making any changes
inventory_backup = copy.deepcopy(inventory)
inventory["Paneer Tikka"]["stock"] = 2
print(inventory)
print(f"\n")
print(inventory_backup)
print(f"\n")

inventory["Paneer Tikka"]["stock"] = 10
#Restored back

#3.2 Simulate order fulfilment: deduct the quantities from the final cart in Task 2 from the corresponding items in inventory.

#Cart in Task 2 was available in
print(cart)

#Start deducting from inventory
for cart_item in cart:
    if(cart_item['item'] not in inventory):
        print(f"Error in Cart. Item - {cart_item['item']} not available in inventory")
        break
    if(inventory[cart_item['item']]['stock'] >= cart_item['quantity']):
        inventory[cart_item['item']]['stock'] = inventory[cart_item['item']]['stock'] - cart_item['quantity']
    else:
        #Stock is low than expected
        low_quantity =  cart_item['quantity'] - inventory[cart_item['item']]['stock']
        inventory[cart_item['item']]['stock'] = 0
        print(f"WARNING for {cart_item['item']}- The low stock is {low_quantity}")

print(f"\n")
print(inventory)
print(f"\n")
#3.3 After deduction, loop through inventory and print a Reorder Alert for every item whose stock is at or below its.

for key,val in inventory.items():
    if(val["stock"] <= val["reorder_level"]):
        print(f"⚠ Reorder Alert: {key} — Only {val["stock"]} unit(s) left (reorder level: {val["reorder_level"]})")

#3.4Print both inventory and inventory_backup at the end to confirm they differ — proving the deep copy protected the original.
print(f"---------------Inventory----------------")
print(inventory)
print(f"\n")
print(f"-----------------inventory Backup--------------")
print(inventory_backup)
print(f"\n")
print(f"-------------------------------")
print(f"they are not the same")
print(f"\n")
print(f"-------------------------------")
print(f"\n")

############################################################################################
#Task 4
#4.1 Print total revenue per day.
revenue_per_day = {}
for key,val in sales_log.items():
    total_per_day = 0
    for order in val:
        total_per_day = total_per_day + order["total"]
    revenue_per_day[key] = total_per_day

print(f"The revenue per day is {revenue_per_day}") 

#4.2 Print the best-selling day (date with the highest total revenue).
max_date = max(revenue_per_day, key=revenue_per_day.get)
print(f"best selling day is {max_date}")
print(f"\n")

#4.3 Find the most ordered item — the item that appears in the greatest number of individual orders across all days.

# We will traverse through the entire data structure sales_log
sales_count = {}
for key,val in sales_log.items():
    for order in val:
        for item in order["items"]:
            if item in sales_count:
                sales_count[item] += 1
            else:
                sales_count[item] = 1
print(sales_count)
max_dish = max(sales_count, key=sales_count.get)
print(f"best selling day is {max_dish}")
print(f"\n")

#4.4
sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"],                     "total": 260.0},
]

revenue_per_day = {}
for key,val in sales_log.items():
    total_per_day = 0
    for order in val:
        total_per_day = total_per_day + order["total"]
    revenue_per_day[key] = total_per_day

print(f"The revenue per day is {revenue_per_day}") 
print(f"\n")
max_date = max(revenue_per_day, key=revenue_per_day.get)
print(f"best selling day is {max_date}")
print(f"\n")

# We will traverse through the entire data structure sales_log
sales_count = {}
for key,val in sales_log.items():
    for order in val:
        for item in order["items"]:
            if item in sales_count:
                sales_count[item] += 1
            else:
                sales_count[item] = 1
print(sales_count)
max_dish = max(sales_count, key=sales_count.get)
print(f"best selling day is {max_dish}")
print(f"\n")

#4.5 Using enumerate, print a numbered list of all orders across all dates (including the new day):
for i, (date, orders) in enumerate(sales_log.items(), start=1):
    for order in orders:
        items = ", ".join(order["items"])
        print(f"{i}.  [{date}] Order #{order['order_id']}  — ₹{order['total']:.2f} — Items: {items}")
        i += 1