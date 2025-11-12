# AC 2nd Order Up

# Setting up the meni
# Define the menu dictionary
menu = {
    # Define another dictionary for drinks
    "Drinks": {
        # List the 4 items with the key and the value as the price
        "Water": 0.00,
        "Fountain Drink": 2.49,
        "Lemonade": 2.79,
        "Sweet Tea": 2.49,
        "Unsweet Tea": 2.49
    },
    # Define another dictionary for the main course
    "Main Courses": {
        "The Box Combo": 11.99,
        "The 3 Finger Combo": 10.39,
        "The Caniac Combo": 17.29,
        "The Sandwich Combo": 10.79,
        "The Kids Combo": 6.99 
    },
    # Define another dictionary for the side dishes
    "Side Dishes": {
        "Chicken Finger": 1.99,
        "Crinkle-Cut Fries": 2.59,
        "Texas Toast": 1.35,
        "Coleslaw": 1.35,
        "Cane's Sauce": 0.39 
    }
}


# Functions
# Function to display the menu
def display_menu(menu_item):
    item_number = 0
    print(f"\n{menu_item}:")
    for i in menu[menu_item]:
        item_number += 1
        print(f"({item_number}) ${menu[menu_item][i]} {i}")

# Calling the functions
# Display the menu
print("Menu:")
display_menu("Drinks")
display_menu("Main Courses")
display_menu("Side Dishes")


#Ordering
total_cost = 0

drink_order = input("\nWhat drink would you like to order?\n")

# USE ITEM NAME INSTEAD OF NUMBER
def ordering(order, menu_item, item, cost):
    if order == 1:
        cost += menu[menu_item][item]
    

ordering(drink_order, "Drinks", "water", total_cost)


#main_course_order = order_input("main course")
#side_dish_order_1 = order_input("first side dish")
#side_dish_order_2 = order_input("second side dish")


# Ask the user what they want as the main course

# Ask the user what they want as their 2 side dishes

# Repeat their order with the total cost.