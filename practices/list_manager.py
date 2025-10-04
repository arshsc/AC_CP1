# AC 2nd Shopping List Manager

shopping_list = []

while True:
    action = input("1. Add item to shopping list:\n2. Remove item from shopping list\n3. Print shopping list\n")
    if action == "1":
        addition_option = input("What single item would you like to add to the list: ")
        shopping_list.append(addition_option)
    elif action == "2":
        remove_option = input("1. Empty list\n 2. Remove singular item?")
        if remove_option == "1":
            shopping_list.clear()
        elif remove_option == "2":
            #pass
            print(shopping_list)
            item_removed = input("What item would you like to be removed from shopping list: ")
            shopping_list.remove(item_removed)
        else:
            print("Enter valid option")
    elif action == "3":
        print(shopping_list)
    elif action == "exit":
        break
    else:
        print("Enter valid option")