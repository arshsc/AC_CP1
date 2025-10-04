# AC 2nd Shopping List Manager

shopping_list = []

while True:
    action = input("\n1. Add item to shopping list:\n2. Remove item from shopping list\n3. Print shopping list\n4. End shopping list\n")
    if action == "1":
        addition_option = input("\nWhat single item would you like to add to the list: ")
        shopping_list.append(addition_option)
        print(shopping_list)
    elif action == "2":
        remove_option = input("\n1. Empty the list\n2. Remove singular item?\n")
        if remove_option == "1":
            shopping_list.clear()
            print(shopping_list)
        elif remove_option == "2":
            #pass
            print(shopping_list)
            item_removed = input("\nWhat item would you like to be removed from shopping list: ")
            shopping_list.remove(item_removed)
            print(shopping_list)
        else:
            print("\nEnter valid option")
    elif action == "3":
        print(shopping_list)
    elif action == "4":
        print(shopping_list)
        break
    else:
        print("\nEnter valid option")