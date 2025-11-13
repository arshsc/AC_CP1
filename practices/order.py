# AC 2nd Order Up

# Setting up the menu
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

# Function to order and add up the cost
def ordering(order, menu_item, cost):
    for item in menu:
        if order in menu[menu_item]:
            cost += menu[menu_item][order]
            return cost
        else:
            print("Invalid Option")
            break


# Calling the functions
# Display the menu
print("Menu:")
display_menu("Drinks")
display_menu("Main Courses")
display_menu("Side Dishes")

# Ordering
# Set cost to $0
total_cost = 0

# Ordering the drinks
drink_order = input("\nWhat drink would you like to order?\n").title()
total_cost += ordering(drink_order, "Drinks", total_cost)

# Ordering the main course
main_course_order = input("\nWhat main course would you like to order?\n").title()
total_cost += ordering(main_course_order, "Main Courses", total_cost)

# Ordering the first side dish
side_dish_order_1 = input("\nWhat first side would you like to order?\n").title()
total_cost += ordering(side_dish_order_1, "Side Dishes", total_cost)

# Ordering the second side dish
side_dish_order_2 = input("\nWhat second side would you like to order?\n").title()
total_cost += ordering(side_dish_order_2, "Side Dishes", total_cost)

# Printing out the reciept
print(f"\nYour Order:\nDrink: {drink_order}\nMain Course: {main_course_order}\nSides:\n{side_dish_order_1}\n{side_dish_order_2}\nTotal Cost: ${total_cost:.2f}")

# Ask the user what they want as the main course

# Ask the user what they want as their 2 side dishes

# Repeat their order with the total cost.