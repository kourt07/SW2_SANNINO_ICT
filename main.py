from pyscript import display

# Restaurant Ordering system using Python Display

# String Data Type
restaurant_name = "Silvers"
owner_name = "KJ Sannino"

# Integer Data Type
year_since = 2027

# Float Data Type
tax_rate = 0.08

# Boolean Data Type
has_delivery = True
is_dine_in = True
is_takeaway= False

# List Data Type
product_names = ["Cake", "Sandwich", "Tea", "Espresso", "Latte"]


# Tuple Data Type
business_hours = ("9:00 AM", "7:00 PM")

# Dictionary Data Type
menu = {
    "Cake": 75.50,
    "Sandwich": 95.00,
    "Tea": 55.00,
    "Espresso": 70.50,
    "Latte": 85.00
}

# Set Data Type
common_allergens = {"nuts", "gluten", "dairy", "soy"}

# Display the restaurant information
display(restaurant_name, target="name1")
display(f"Owner: {owner_name}", target="owner")
display(f"Since: {year_since}", target="since")   
display(f"Menu Pricelist", target="heading1")



# Display menu items
display(product_names[0], target="prod1")
display(f"₱{menu['Cake']}", target="price1")

display(product_names[1], target="prod2")
display(f"₱{menu['Sandwich']}", target="price2")

display(product_names[2], target="prod3")
display(f"₱{menu['Tea']}", target="price3")

display(product_names[3], target="prod4")
display(f"₱{menu['Espresso']}", target="price4")

display(product_names[4], target="prod5")
display(f"₱{menu['Latte']}", target="price5")

# Display additional information
display(f"Open: {business_hours[0]} - {business_hours[1]}", target="openingHours")

display(f"Dine-In Available: {is_dine_in}", target="orderType")