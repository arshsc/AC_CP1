# AC 2nd Order Up


# Setting up the menu
# Dictionary for the menu
menu = {
    # Define a nested dictionary for the drinks
    "Drinks": {
        # List the items with the key and the value as the price
        "Water": 0.00,
        "Fountain Drink": 2.49,
        "Lemonade": 2.79,
        "Sweet Tea": 2.49,
        "Unsweet Tea": 2.49
    },
    # Define a nested dictionary for the main course
    "Main Courses": {
        "The Box Combo": 11.99,
        "The 3 Finger Combo": 10.39,
        "The Caniac Combo": 17.29,
        "The Sandwich Combo": 10.79,
        "The Kids Combo": 6.99 
    },
    # Define a nested dictionary for the side dishes
    "Side Dishes": {
        "Chicken Finger": 1.99,
        "Fries": 2.59,
        "Texas Toast": 1.35,
        "Coleslaw": 1.35,
    }
}


# Functions
# Function to display the menu
def display_menu(menu_item):
    print(f"\n{menu_item}:")
    for i in menu[menu_item]:
        print(f"${menu[menu_item][i]} {i}")

# Function to order and add up the cost
def ordering(menu_item, prompt=None):
    while True:
        if prompt:
            order = input(f"\nWhat {prompt} would you like to order? (Type in the name)\n").title().strip()
        else:
            order = input(f"\nWhat {menu_item[:-1].lower()} would you like to order? (Type in the name)\n").title().strip()
        if order in menu[menu_item]:
            return menu[menu_item][order], order
        print("Invalid Option, Retry")


# Calling the functions
# Display the menu
print("Menu:")
display_menu("Drinks")
display_menu("Main Courses")
display_menu("Side Dishes")

# Ordering
total_cost = 0.00

# Drinks
cost, drink_order = ordering("Drinks")
total_cost += cost

# Main Course
cost, main_course_order = ordering("Main Courses")
total_cost += cost

# Side Dishes
cost, side_dish_order_1 = ordering("Side Dishes", prompt="first side")
total_cost += cost

cost, side_dish_order_2 = ordering("Side Dishes", prompt="second side")
total_cost += cost

# Printing out the receipt
print(f"\nYour Order:\nDrink: {drink_order}\nMain Course: {main_course_order}\nSides:\n{side_dish_order_1}\n{side_dish_order_2}\nTotal Cost: ${total_cost:.2f}")