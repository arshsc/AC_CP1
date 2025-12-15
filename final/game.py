# AC 2nd Final Project Text Adventure Game

# import needed libraries
import random

# combat
def servant_combat(player_health, player_stamina, player_weapon_chosen):

    ghost_health = 100
    base_player_damage = inventory["Weapons"][player_weapon_chosen]

    print("\n" *20)
    print("\nThe servant ghost turns toward you.")
    print("\n\"You should not be here!\" it yells.")
    print(f"\n Weapon Equipped: {player_weapon_chosen} (+{inventory['Weapons'][player_weapon_chosen]} DMG)")

    while True:
        fight_confirm = input("\n     - Yes\n     - No\n\nAre you sure you want to fight the ghost: ").strip().lower()
        if fight_confirm in ["yes", "y"]:
            print("\n" *20)
            print("\nYou step forward to him.")
            break
        elif fight_confirm in ["no", "n"]:
            print("\n" *20)
            print("\nYou take a step back, then turn around to run back into the mansion.")
            return player_health, player_stamina, False
        else:
            print("Please type Yes or No.")

    # Randomly decide who goes first
    turn = random.randint(1, 2)

    while ghost_health > 0 and player_health > 0:

        if turn == 1:
            print("\n\nYour Turn:")
            print(f"Your Health: {player_health}")
            print(f"Your Stamina: {player_stamina}")
            print(f"\nGhost Health: {ghost_health}")

            if player_stamina <= 0:
                print("\n" *20)
                print("\nYou are too exhausted to move!")
                player_stamina += 2
                print("You regain 2 stamina.")
                turn = 2
                continue

            choice = input("\nActions:\n\n    - Quick Slash\n    - Charge Attack\n    - Consumable\n\nChoose an action: "
            ).lower().strip()

            if choice == "quick slash":
                damage = base_player_damage + random.randint(2, 7)
                player_stamina -= 1
                ghost_health -= damage
                print("\n" *20)
                print(f"\nYou dash forward and slash the ghost for {damage} damage!\n")

            elif choice == "charge attack":
                if player_stamina < 4:
                    print("\n" *20)
                    print("\nYou are too exhausted to move!")
                    turn = 2
                    continue
                damage = base_player_damage + random.randint(6, 12)
                player_stamina -= 3
                ghost_health -= damage
                print("\n" *20)
                print(f"\nYou charge your weapon and strike for {damage} damage!")

            elif choice == "consumable":
                available_consumables = []
                if len(inventory["Consumables"]["Bandage"]) > 0:
                    available_consumables.append(f"Bandage (+{inventory['Consumables']['Bandage'][0]} HP) x{len(inventory['Consumables']['Bandage'])}")
                if len(inventory["Consumables"]["Energy Drink"]) > 0:
                    available_consumables.append(f"Energy Drink (+{inventory['Consumables']['Energy Drink'][0]} Stamina) x{len(inventory['Consumables']['Energy Drink'])}")

                if not available_consumables:
                    print("\n" *20)
                    print("\nYou have no consumables!")
                    continue

                print("\n" *20)
                print("\nYour consumables:")
                for item in available_consumables:
                    print(f" - {item}")

                use = input("\nWhich consumable would you like to use? ").lower().strip()

                if use == "bandage" and len(inventory["Consumables"]["Bandage"]) > 0:
                    heal = inventory["Consumables"]["Bandage"].pop()
                    player_health += heal
                    if player_health > 50:
                        player_health = 50
                    print("\n" *20)
                    print(f"\nYou heal yourself for {heal} HP.")

                elif use == "energy drink" and len(inventory["Consumables"]["Energy Drink"]) > 0:
                    stam = inventory["Consumables"]["Energy Drink"].pop()
                    player_stamina += stam
                    print("\n" *20)
                    print(f"\nYou regain {stam} stamina.")

                else:
                    print("\n" *20)
                    print("\nInvalid consumable choice.")

            else:
                print("\n" *20)
                print("\nInvalid action.")
                continue

            if ghost_health <= 0:
                print("\nThe servant yells and then faded away into thin air. Something drops from where the servant once stood.")
                inventory["Keys"].append("Rail Key")
                print("\n(+) Rail Key")
                return player_health, player_stamina, True

            turn = 2

        else:
            print("\nServant's Turn:")

            ghost_choice = random.randint(1, 2)

            if ghost_choice == 1:
                damage = random.randint(4, 7)
                print("The servant slashes at you with the butter knife!")
            else:
                damage = random.randint(8, 14)
                print("The servant charges and smashes the metal plate onto your head!")
            if random.randint(1, 100) <= 25:
                print("The servant’s attack passes through you!")
                damage = 0

            player_health -= damage
            print(f"You take {damage} damage!")

            # Check if player is dead
            if player_health <= 0:
                print("\n\nYOU HAVE DIED.\n")
                return 0, player_stamina, False

            turn = 1


# trailer home
def trailer_home(bathroom_searched, storage_cabinet_searched, main_area_searched):

    location = "Trailer Home"
    
    print("\n" *20)
    print("You walk over towards the trailer home. The door is unlocked and you walk in.")
    print("\nThis is a very small trailer home. The walls are yellow with dirt scattered all throughout the inside.")

    while location == "Trailer Home":

        while True:
            search = input("\nThere are 3 areas worth searching.\n   \n     - Bathroom   \n     - Storage Cabinet   \n     - Main Area     \n     - Exit\n\nWhere would you like to go: ").lower().strip()

            if search in ["bathroom", "storage cabinet", "main area", "exit"]:
                break
            else:
                print("\n" *20)
                print("\nThat is not a room, please retry.")

        while True:
            if search == "bathroom":
                if bathroom_searched == False:
                    bathroom_searched = True
                    print("\n" *20)
                    print("\nYou enter the cramped bathroom. Near the sink, there is a bandage. You pick it up and put it in your backpack. Nothing else is in here and you exit.\n\n(+) Bandage")
                    inventory["Consumables"]["Bandage"].append(10)
                    break
                elif bathroom_searched == True:
                    print("\n" *20)
                    print("\nYou already searched the bathroom, you picked up the bandage and nothing else is to be found.")
                    break

            elif search == "storage cabinet":
                if storage_cabinet_searched == False:
                    storage_cabinet_searched = True
                    print("\n" *20)
                    print("\nYou open the big storage cabinet. Old clothes and jackets scatter the insides. You dig through the old clothes and find a key with an engraving that says \"School Front Door\". You stash it in your backpack.\n\n(+) School Front Door Key")
                    inventory["Keys"].append("School Key")
                    break
                elif storage_cabinet_searched == True:
                    print("\n" *20)
                    print("\nYou have already searched the storage cabinet and found a key engraved with \"School Front Door\".")
                    break

            elif search == "main area":
                if main_area_searched == False:
                    main_area_searched = True
                    print("\n" *20)
                    main_area_note = input("\nYou look around your surroundings. On the small dining table there is a note available to read.\n\n     - Yes     \n     - No \n\nWould you like to read it: ").strip().lower()
                    if main_area_note in ["yes", "y"]:
                        print("\n" *20)
                        print("\n\"Dear #$&@!#$,\nI overheard one of my 3rd grade students talking about something dark. I heard about an axe that has special properties. This could all be a hoax, I am not sure. It might be worth your time to go check on the student's parents.\"")
                        break
                    elif main_area_note in ["no", "n"]:
                        print("\n" *20)
                        print("You put the note back down.")
                        break
                    else:
                        print("\nInvalid Option.")
                        continue
                elif main_area_searched == True:
                    print("\n" *20)
                    main_area_note = input("\nThere is nothing else here besides the note\n\n     - Yes     \n     - No \n\nWould you like to read the note: ")
                    if main_area_note in ["yes", "y"]:
                        print("\n" *20)
                        print("\n\"Dear #$&@!#$,\nI overheard one of my 3rd grade students talking about something dark. I heard about an axe that has special properties. This could all be a hoax, I am not sure. It might be worth your time to go check on the student's parents.\"")
                        break
                    elif main_area_note in ["no", "n"]:
                        print("\n" *20)
                        print("You put the note back down.")
                        break
                    else:
                        print("\nInvalid Option.")
                        continue

            elif search == "exit":
                print("\n" *20)
                print("\nYou exit the trailer home")
                location = "Town"
                break

            else:
                print("\n" *20)
                print("\nThat is not a valid option, please retry.")
                break
    return bathroom_searched, storage_cabinet_searched, main_area_searched

# collapsed house
def collapsed_house(living_room_searched, bedroom_searched, rubble_pile_searched):

    location = "Collapsed House"
    
    print("\n" *20)
    print("You walk over towards the collapsed house. The door is unlocked and you walk in.")
    print("\nAll that is left is a few standing wall. The roof has caved in.")

    while location == "Collapsed House":

        while True:
            search = input("\nThere are 3 areas worth searching.\n   \n     - Living Room   \n     - Bedroom   \n     - Rubble Pile     \n     - Exit\n\nWhere would you like to go: ").lower().strip()

            if search in ["living room", "bedroom", "rubble pile", "exit"]:
                break
            else:
                print("\n" *20)
                print("\nThat is not a room, please retry.")

        while True:
            if search == "living room":
                if living_room_searched == False:
                    living_room_searched = True
                    print("\n" *20)
                    print("\nYou enter the wide living room. There is not much here besides a table and a few couches covered in rubble. Nothing is found here worth to take.")
                    break
                elif living_room_searched == True:
                    print("\n" *20)
                    print("\nYou already searched the living room, nothing was here to be found.")
                    break

            elif search == "bedroom":
                if bedroom_searched == False:
                    bedroom_searched = True
                    print("\n" *20)
                    print("\nYou walk into a lone doorway with no wall, this seems to be the master bedroom of the house. You see a dresser barely visible from all the rubble. You walk to it, dig to the dresser drawer and inside you find a bandage.\n\n(+) Bandage")
                    inventory["Consumables"]["Bandage"].append(10)
                    break
                elif bedroom_searched == True:
                    print("\n" *20)
                    print("\nYou have already searched the bedroom and found the bandage.")
                    break

            elif search == "rubble pile":
                if rubble_pile_searched == False:
                    rubble_pile_searched = True
                    print("\n" *20)
                    print("\nYou see a suspicious looking rubble pile. You dig through and find an unlocked chest, and in this chest is a key labeled \"Library\"\n\n(+) Library Key")
                    inventory["Keys"].append("Library Key")
                    break
                elif rubble_pile_searched == True:
                    print("\n" *20)
                    print("\nYou have already searched the rubble pile and found the library key.")
                    break

            elif search == "exit":
                print("\n" *20)
                print("\nYou exit the collapsed house")
                location = "Town"
                break

            else:
                print("\n" *20)
                print("\nThat is not a valid option, please retry.")
                break
    return living_room_searched, bedroom_searched, rubble_pile_searched

# mansion
def mansion(master_bedroom_searched, vault_searched, garden_searched, player_weapon_chosen, player_health, player_stamina, servant_defeated):


    location = "Mansion"
    
    print("\n" *20)
    print("You walk over towards the mansion. The door is unlocked and you walk in.")
    print("\nThis house is huge. An endless hallway greets you, but most of the hallway seems to be blocked.")

    while location == "Mansion":

        while True:
            search = input("\nThere are 3 areas worth searching.\n   \n     - Master Bedroom   \n     - Vault   \n     - Garden     \n     - Exit\n\nWhere would you like to go: ").lower().strip()

            if search in ["master bedroom", "vault", "garden", "exit"]:
                break
            else:
                print("\n" *20)
                print("\nThat is not a room, please retry.")

        while True:
            if search == "master bedroom":
                if master_bedroom_searched == False:
                    master_bedroom_searched = True
                    print("\n" *20)
                    print("\nYou enter the massive bedroom. There is elegant furniture throughout the whole room. You open the nightstand and find a key labeled \"Train Station\".\n\n(+) Train Station Key")
                    inventory["Keys"].append("Train Station Key")
                    break
                elif master_bedroom_searched == True:
                    print("\n" *20)
                    print("\nYou already searched the master bedroom, you picked up the \"Train Station\" and nothing else is to be found.")
                    break

            elif search == "vault":
                if vault_searched == False:
                    vault_searched = True
                    print("\n" *20)
                    print("\nYou walk down the grand stairs into the basement. The only thing in this basement is a giant vault door, slightly cracked open. You peek in and see an intact glass showcase with an axe. This is not an ordinary axe, it has a mysterious dark aura around it. You pick it up and feel an eerie feeling.\n\n(+) Ghost Axe")
                    inventory["Weapons"]["Ghost Axe"] = 15
                    while True:
                        weapon_choice = input("\n     - Dagger (+10 DMG)\n     - Ghost Axe (+15 DMG)\n\nWhich weapon would you like to use: ").strip().title()
                        if weapon_choice == "Dagger":
                            print("\n" *20)
                            print("\nYou stash the Ghost Axe into your backpack.")
                            break
                        if weapon_choice == "Ghost Axe":
                            print("\n" *20)
                            print("\nYou stash your dagger into your backpack and hold the Ghost Axe.")
                            player_weapon_chosen = "Ghost Axe"
                            break
                    break
                elif vault_searched == True:
                    print("\n" *20)
                    print("\nYou have already searched the vault and found the Ghost Axe")
                    break

            elif search == "garden":
                if not garden_searched:
                    print("You enter the vibrant garden behind the mansion.")
                    if not servant_defeated:
                        player_health, player_stamina, fought = servant_combat(player_health, player_stamina, player_weapon_chosen)
                        if fought:
                            servant_defeated = True
                    garden_searched = True

                print("\nThe servant has been defeated. The garden is peaceful now.")

                leave = input("\n     - Yes     \n     - No \n\nDo you want to leave the garden and return to the mansion? ").strip().lower()
                if leave in ["yes", "y"]:
                    print("\n" *20)
                    break
                elif leave in ["no", "n"]:
                    print("\nYou stay in the garden. Think carefully.")
                else:
                    print("\nInvalid input.")

            elif search == "exit":
                print("\n" *20)
                print("\nYou exit the Mansion")
                location = "Town"
                break

            else:
                print("\n" *20)
                print("\nThat is not a valid option, please retry.")
                break

    return master_bedroom_searched, vault_searched, garden_searched, player_weapon_chosen, player_health, player_stamina, servant_defeated

# prison
def prison(kitchen_searched, cell_hallway_searched, cell_searched):

    location = "Prison"
    
    print("\n" *20)
    print("You walk over towards the massive prison gates. The door is locked but it seems easy to climb, so you do so and get in.")
    print("\nThis prison is huge. A lot of it is boarded up and not too many rooms are available.")

    while location == "Prison":

        while True:
            search = input("\nThere are 3 areas worth searching.\n   \n     - Kitchen   \n     - Cell Hallway   \n     - Cell     \n     - Exit\n\nWhere would you like to go: ").lower().strip()

            if search in ["kitchen", "cell hallway", "cell", "exit"]:
                break
            else:
                print("\n" *20)
                print("\nThat is not a room, please retry.")

        while True:
            if search == "kitchen":
                if kitchen_searched == False:
                    kitchen_searched = True
                    print("\n" *20)
                    print("\nYou enter the kitchen. It is filthy, but some food could be nice. You open the storage room and see a bunch of food. You pick some up and realize they all expired decades ago.")
                    break
                elif kitchen_searched == True:
                    print("\n" *20)
                    print("\nYou already searched the kitchen. Nothing was to be found")
                    break

            elif search == "cell hallway":
                if cell_hallway_searched == False:
                    cell_hallway_searched = True
                    print("\n" *20)
                    print("\nYou walk to the massive hallway. Cells on each side with a second story of more cells. On the side near the emergency exit, there seems to be some sort of battery. You pick it up.\n\n(+) Battery")
                    inventory["Items"].append("Battery")
                    break
                elif cell_hallway_searched == True:
                    print("\n" *20)
                    print("\nYou have already searched the cell hallway and found a battery.")
                    break

            elif search == "cell":
                if cell_searched == False:
                    cell_searched = True
                    print("\n" *20)
                    print("\nYou walk into one of the only cells not blocked. You search the small table and under the bed. You find a single wire under the bed. \n\n(+) Wire")
                    inventory["Items"].append("Wire")
                    break
                elif cell_searched == True:
                    print("\n" *20)
                    print("\nYou have already searched the cell and found a wire.")
                    break

            elif search == "exit":
                print("\n" *20)
                print("\nYou exit the Prison")
                location = "Town"
                break

            else:
                print("\n" *20)
                print("\nThat is not a valid option, please retry.")
                break
    return kitchen_searched, cell_hallway_searched, cell_searched

# school
def school(classroom_searched, school_library_searched, office_searched, cafeteria_searched):

    location = "School"
    
    print("\n" *20)
    print("You walk over towards the school. You use your school key and it works, the front door opens.")
    print("\nThis is a relatively small and very old school.")

    while location == "School":

        while True:
            search = input("\nThere are 4 areas worth searching.\n   \n     - Classroom   \n     - School Library   \n     - Office     \n     - Cafeteria     \n     - Exit\n\nWhere would you like to go: ").lower().strip()

            if search in ["classroom", "school library", "office", "cafeteria", "exit"]:
                break
            else:
                print("\n" *20)
                print("\nThat is not a room, please retry.")

        while True:

            if search == "classroom":
                if classroom_searched == False:
                    classroom_searched = True
                    print("\n" *20)
                    print("\nYou enter the classroom. The roof seems that it is about to cave in. On one of the desks, there is an unopened energy drink that seems new. You pick it up and put it in your backpack.\n\n(+) Energy Drink")
                    inventory["Consumables"]["Energy Drink"].append(4)
                    break
                elif classroom_searched == True:
                    print("\n" *20)
                    print("\nYou already searched the classroom, you picked up the energy drink and nothing else is to be found.")
                    break

            elif search == "school library":
                if school_library_searched == False:
                    school_library_searched = True
                    print("\n" *20)
                    print("\nYou walk into the tiny library. The bookshelves are on the floor, and many books scattered through the floor. Nothing useful seems to be in here.")
                    break
                elif school_library_searched == True:
                    print("\n" *20)
                    print("\nYou have already searched the library and nothing was to be found.")
                    break

            elif search == "office":
                if office_searched == False:
                    office_searched = True
                    print("\n" *20)
                    office_note = input("\nYou can't enter the office as it is locked shut. you peek over the front desk and find a note.\n\n     - Yes     \n     - No \n\nWould you like to read the note: ").strip().lower()
                    if office_note in ["yes", "y"]:
                        print("\n" *20)
                        print("\n\"THE MINES HOLD #$%&!@# AND %$#@, SOMETHING PROTECTS IT.\"")
                        break
                    elif office_note in ["no", "n"]:
                        print("\n" *20)
                        print("You put the note back down.")
                        break
                elif office_searched == True:
                    print("\n" *20)
                    office_note = input("\nThere is nothing else here besides the note.\n\n     - Yes     \n     - No \n\nWould you like to read the note: ")
                    if office_note in ["yes", "y"]:
                        print("\n" *20)
                        print("\n\"WHAT NOTE SAYS!\"")
                        break
                    elif office_note in ["no", "n"]:
                        print("\n" *20)
                        print("\nYou put the note down.")
                        break
            elif search == "cafeteria":
                if cafeteria_searched == False:
                    cafeteria_searched = True
                    print("\n" *20)
                    print("\nYou walk into the cafeteria. It has been stripped from every appliance and barely a kitchen now. You see a dangling wire and grab it.\n\n(+) Wire")
                    inventory["Items"].append("Wire")
                    break
                elif cafeteria_searched == True:
                    print("\n" *20)
                    print("\nYou have already searched the cafeteria and nothing was to be found.")
                    break

            elif search == "exit":
                print("\n" *20)
                print("\nYou exit the school")
                location = "Town"
                break

            else:
                print("\n" *20)
                print("\nThat is not a valid option, please retry.")
                break
    return classroom_searched, school_library_searched, office_searched, cafeteria_searched

# library
def library(bookshelf_searched, theatre_stage_searched, front_desk_searched):

    location = "Library"
    
    print("\n" *20)
    print("You walk over towards the library. The door is locked but you use your library key and enter the room.")
    print("\nThis place seems to be the most intact place in this town. The bookshelves are filled with old books, although some are scattered throughout the floor.")

    while location == "Library":

        while True:
            search = input("\nThere are 3 areas worth searching.\n   \n     - Bookshelf   \n     - Theatre Stage   \n     - Front Desk     \n     - Exit\n\nWhere would you like to go: ").lower().strip()

            if search in ["bookshelf", "theatre stage", "front desk", "exit"]:
                break
            else:
                print("\n" *20)
                print("\nThat is not a room, please retry.")

        while True:
            if search == "bookshelf":
                if bookshelf_searched == False:
                    bookshelf_searched = True
                    print("\n" *20)
                    print("\nYou walk through the rows of bookshelves, searching for something useful. After going through the majority of the library, nothing useful was found.")
                    break
                elif bookshelf_searched == True:
                    print("\n" *20)
                    print("\nYou already searched the bookshelves, nothing was here to be found.")
                    break

            elif search == "theatre stage":
                if theatre_stage_searched == False:
                    theatre_stage_searched = True
                    print("\n" *20)
                    print("\nYou walk over the the theatre stage. the floorboards are cracked with some missing. You see a dangling wire on the right and decide to take it.\n\n(+) Wire")
                    inventory["Items"].append("Wire")
                    break
                elif theatre_stage_searched == True:
                    print("\n" *20)
                    print("\nYou have already searched the theatre stage and found a wire.")
                    break

            elif search == "front desk":
                if front_desk_searched == False:
                    front_desk_searched = True
                    print("\n" *20)
                    print("\nYou walk over to the front desk of the library. An unopened energy drink that seems relatively new, you decide to take it.\n\n(+) Energy Drink")
                    inventory["Consumables"]["Energy Drink"].append(4)
                    break
                elif front_desk_searched == True:
                    print("\n" *20)
                    print("\nYou have already searched the front desk and found the energy drink.")
                    break

            elif search == "exit":
                print("\n" *20)
                print("\nYou exit the library")
                location = "Town"
                break

            else:
                print("\n" *20)
                print("\nThat is not a valid option, please retry.")
                break
    return bookshelf_searched, theatre_stage_searched, front_desk_searched

# train station
def train_station(ticket_office_searched, boarding_area_searched):

    location = "Train Station"
    
    print("\n" *20)
    print("\nYou walk over towards the train station. The door is locked but you use your train station key to enter.")
    print("\nThere is an immense amount of dust everywhere with cobwebs all over the inside.")

    while location == "Train Station":

        while True:
            search = input("\nThere are 2 areas worth searching.\n   \n     - Ticket Office   \n     - Boarding Area   \n     - Exit\n\nWhere would you like to go: ").lower().strip()

            if search in ["ticket office", "boarding area", "exit"]:
                break
            else:
                print("\n" *20)
                print("\nThat is not a room, please retry.")

        while True:
            if search == "ticket office":
                if ticket_office_searched == False:
                    ticket_office_searched = True
                    print("\n" *20)
                    print("\nYou use the train station key once again to enter the ticket office. On the desk, there is an energy drink and bandage left there. You grab it and put it in your backpack.\n\n(+) Energy Drink\n\n(+) Bandage")
                    inventory["Consumables"]["Energy Drink"].append(4)
                    inventory["Consumables"]["Bandage"].append(10)
                    break
                elif ticket_office_searched == True:
                    print("\n" *20)
                    print("\nYou already searched the ticket office and found the energy drink and bandage.")
                    break

            elif search == "boarding area":
                if boarding_area_searched == False:
                    boarding_area_searched = True
                    print("\n" *20)
                    print("\nYou walk outside onto the boarding area. On the wall to your left is a lever for the train. You decide to pull it and then it falls off, and then you pick it up and put it in your backpack.\n\n(+) Lever")
                    inventory["Items"].append("Lever")
                    break
                elif boarding_area_searched == True:
                    print("\n" *20)
                    print("\nYou have already searched the boarding area and found a lever.")
                    break

            elif search == "exit":
                print("\n" *20)
                print("\nYou exit the train station")
                location = "Town"
                break

            else:
                print("\n" *20)
                print("\nThat is not a valid option, please retry.")
                break
    return ticket_office_searched, boarding_area_searched

# entrance of mine
def entrance_of_mine(cart_station_searched, railroad_searched, cart_on_rails):

    location = "Entrance of the Mines"
    enter_mines = False 
    print("\n" *20)
    print("You walk to the entrance of the mines. The lever to open the gate is broken. You pull it off and insert the lever you stored in your backpack. You flick the lever and the gate opens.")
    print("\nThere is a narrow hallway leading to the railroad with a few carts on the sides.")

    while location == "Entrance of the Mines":
        search = input("\nThere are 2 areas worth searching.\n   \n     - Cart Station   \n     - Railroad   \n     - Exit\n\nWhere would you like to go: ").lower().strip()

        if search == "cart station":
            if not cart_station_searched:
                cart_station_searched = True
                print("\n" *20)
                print("You turn the corner to the cart station. A bunch of old carts are left here. You need one to go down into the mines. You put a cart onto the rails.")
                cart_on_rails = True
            else:
                print("\n" *20)
                print("You already put a cart on the rails.")

        elif search == "railroad":
            if not railroad_searched:
                railroad_searched = True

            if not cart_on_rails:
                print("\n" *20)
                print("You walk to the rails and see it goes into a dark tunnel. You don't have a cart to go in.")
            else:
                print("\n" *20)
                go_into_mines = input("\nYou are ready to go down into the mines\n\n     - Yes\n     - No\n\nWould you like to: ").strip().lower()
                if go_into_mines in ["yes", "y"]:
                    wire_count = inventory["Items"].count("Wire")
                    battery_found = "Battery" in inventory["Items"]
                    rail_key = "Rail Key" in inventory["Items"]

                    if wire_count >= 3 and battery_found and rail_key:
                        enter_mines = True
                        break
                    else:
                        missing = []
                        if wire_count < 3:
                            missing.append(f"{3 - wire_count} Wire(s)")
                        if not battery_found:
                            missing.append("Battery")
                        if not rail_key:
                            missing.append("Rail Key")

                        print("\n" *20)
                        print("You are missing the following items:")
                        for item in missing:
                            print(f"     - {item}")
                        print("You cannot enter the mines yet.")

                elif go_into_mines in ["no", "n"]:
                    continue
                else:
                    print("\nInvalid input.")

        elif search == "exit":
            print("\n" *20)
            print("You exit the entrance of the mines")
            location = "Town"
            break

        else:
            print("\n" *20)
            print("That is not a valid option, please retry.")

    return cart_station_searched, railroad_searched, cart_on_rails, enter_mines

# underground railroad
def underground_railroad(wire_count, battery_found, miner_health, miner_damage, player_health, player_stamina, player_weapon_chosen):
    
    location = "Underground Railroad"
    miner_defeated = False

    print("\n" *20)
    print("You arrive at the Underground Railroad. It is dark, damp, and full of old mining equipment.")
    
    # Check if player has enough items to access
    if wire_count < 3 or not battery_found:
        print("\nYou need at least 3 wires and a battery to power the gates and proceed further.")
        return wire_count, battery_found, miner_health, player_health, player_stamina, miner_defeated

    print("\nYou connect the 3 wires and the battery to the power system. The gates hum and open, revealing the tunnels deeper underground.")

    while location == "Underground Railroad":
        
        search = input("\nThere is a path deeper into the tunnels.\n\n   - Proceed\n   - Exit\n\nWhere would you like to go: ").lower().strip()

        if search == "exit":
            print("\n" *20)
            print("\nYou go back to the surface. You can revisit all previously explored locations.")
            location = "Town"
            break

        elif search == "proceed":
            if miner_defeated == False:
                print("\n" *20)
                print("As you go deeper, a massive miner blocks your path. He is guarding the valuable gems!")
                
                # Combat with final boss
                while miner_health > 0 and player_health > 0:

                    print(f"\nYour Health: {player_health} | Stamina: {player_stamina}")
                    print(f"Miner Health: {miner_health}")

                    choice = input("\nChoose an action:\n   - Quick Attack\n   - Charge Attack\n   - Consumable\n\nAction: ").lower().strip()

                    if choice == "quick attack":
                        damage = inventory["Weapons"][player_weapon_chosen] + 5
                        player_stamina -= 1
                        miner_health -= damage
                        print(f"\nYou quickly attack the miner for {damage} damage!")

                    elif choice == "charge attack":
                        if player_stamina < 3:
                            print("\nNot enough stamina for a charge attack!")
                            continue
                        damage = inventory["Weapons"][player_weapon_chosen] + 10
                        player_stamina -= 3
                        miner_health -= damage
                        print(f"\nYou charge and strike the miner for {damage} damage!")

                    elif choice == "consumable":
                        if len(inventory["Consumables"]["Bandage"]) == 0 and len(inventory["Consumables"]["Energy Drink"]) == 0:
                            print("\nNo consumables left!")
                        else:
                            use = input("\nUse Bandage or Energy Drink: ").lower().strip()
                            if use == "bandage" and len(inventory["Consumables"]["Bandage"]) > 0:
                                heal = inventory["Consumables"]["Bandage"].pop()
                                player_health += heal
                                print(f"\nYou heal yourself for {heal} HP.")
                            elif use == "energy drink" and len(inventory["Consumables"]["Energy Drink"]) > 0:
                                stam = inventory["Consumables"]["Energy Drink"].pop()
                                player_stamina += stam
                                print(f"\nYou regain {stam} stamina.")
                            else:
                                print("\nInvalid choice.")
                        continue

                    else:
                        print("\nInvalid action, try again.")
                        continue

                    # Miner attacks
                    if miner_health > 0:
                        m_attack = random.randint(25, 50)
                        player_health -= m_attack
                        print(f"\nThe miner attacks you for {m_attack} damage!")
                        if player_health <= 0:
                            print("\nYou have been defeated by the miner...")
                            return wire_count, battery_found, miner_health, player_health, player_stamina, miner_defeated

                print("\nYou defeated the miner! You collect the valuable gems and can now leave the town or return later.")
                inventory["Items"].append("Valuable Gems")
                miner_defeated = True

            elif miner_defeated == True:
                print("\nThe miner has already been defeated. You can take the gems and leave or explore the tunnels freely.")

    return wire_count, battery_found, miner_health, player_health, player_stamina, miner_defeated

# intro
def intro_monologue():
    print("\nYou heard of a rumor about an abandoned, small, ghost town 20 minutes away from your home town having valuable gems somewhere deep in the mines. No one has dared to go retrieve the valuable gems as there are spirits preventing you from going into the mines. Many deaths have been reported at this town.\n\nYou decide you want to go.\n\nYou inform your family and friends, they all try to stop you but you are determined.\n\nYou pack your bag with these items.\n\n     - Dagger\n     - Bandage\n     - Energy Drink\n     - Phone\n\nYou set out and get to the town. Your adventure begins.\n\nYou arrive to the desolate town. Buildings are boarded up, the roads have a layer of sand and dirt, no one has stepped foot here in years. You take out your phone to call your family. The call rings infinitely, your phone has no service. It is just you, all alone.")

# inventory
def show_inventory(player_weapon_chosen):

    print(f"Weapon in use: {player_weapon_chosen}")
    print("\nWeapons:")
    for weapon, dmg in inventory["Weapons"].items():
        print(f" - {weapon}: +{dmg} DMG")

    print("\nConsumables:")
    for item, effects in inventory["Consumables"].items():
        if len(effects) == 0:
            print(f" - {item}: None")
        else:
            effect_value = effects[0]
            unit = "HP" if item == "Bandage" else "Stamina"
            print(f" - {item} (+{effect_value} {unit}) x{len(effects)}")

    print("\nKeys:")
    if len(inventory["Keys"]) == 0:
        print(" - None")
    else:
        for key in inventory["Keys"]:
            print(f" - {key}")

    print("\nItems:")
    if len(inventory["Items"]) == 0:
        print(" - None")
    else:
        for item in inventory["Items"]:
            print(f" - {item}")

# room input and inventory function
def room_input(locations, player_weapon_chosen):

    random.shuffle(locations)

    while True:

        print("\nThese locations look worth exploring.\n")

        for l in locations:
            print(f"     - {l}")
        print("\nTo see what is in your backpack")
        print("\n     - Inventory")

        choice = input("\nWhat building would you like to go to: ").title().strip()

        if choice.lower() in ["inventory", "inv", "i"]:
            print("\n" *20)
            show_inventory(player_weapon_chosen)
            continue

        if choice not in locations:
            print("\n" *20)
            print("\nThat place doesn't exist, choose another place.")
            continue

        return choice

# game loop
while True:
    # dictionary for the inventory
    inventory = {
        "Weapons": {
            "Dagger": 10
        },
        "Consumables": {
            "Bandage": [10],
            "Energy Drink": [4]
        },
        "Keys": [],
        "Items": []
    }

    # player stats
    player_health = 50
    player_damage = random.randint(1, 10)
    player_stamina = 10
    player_weapon_chosen = "Dagger"


    # servant stats (first boss)
    servant_defeated = False
    servant_health = 150
    servant_damage = random.randint(1, 20)


    # miner stats (final boss)
    miner_health = 250
    miner_damage = random.randint(25, 50)

    # list of all locations
    locations = ["Trailer Home", "Collapsed House", "Mansion", "Prison", "School", "Library", "Train Station", "Entrance Of The Mines", "Underground Railroad"]
    location = "Town"

    # trailer home
    trailer_home_searched = False
    bathroom_searched = False
    storage_cabinet_searched = False
    main_area_searched = False

    # collapsed house
    collapsed_house_searched = False
    living_room_searched = False
    bedroom_searched = False
    rubble_pile_searched = False

    # mansion
    mansion_searched = False
    master_bedroom_searched = False
    vault_searched = False
    garden_searched = False

    # prison
    prison_searched = False
    kitchen_searched = False
    cell_hallway_searched = False
    cell_searched = False

    # school
    school_searched = False
    classroom_searched = False
    school_library_searched = False
    office_searched = False
    cafeteria_searched = False

    # library
    library_searched = False
    bookshelf_searched = False
    theatre_stage_searched = False
    front_desk_searched = False

    # train station
    train_station_searched = False
    ticket_office_searched = False
    boarding_area_searched = False

    # entrance of the mine
    entrance_of_the_mine_searched = False
    cart_station_searched = False
    railroad_searched = False
    cart_on_rails = False

    # underground railroad
    underground_railroad_searched = False


    # start to play the game
    intro_monologue()

    while True:

        if player_health <= 0:
            print("\nYou have died. Game Over.")
            break

        location = room_input(locations, player_weapon_chosen)

        if location == "Trailer Home":
            if not trailer_home_searched:
                bathroom_searched, storage_cabinet_searched, main_area_searched = trailer_home(bathroom_searched, storage_cabinet_searched, main_area_searched)
                trailer_home_searched = True
            else:
                print("\n" *20)
                print("\nYou have already searched the Trailer Home.")
                bathroom_searched, storage_cabinet_searched, main_area_searched = trailer_home(bathroom_searched, storage_cabinet_searched, main_area_searched)

        elif location == "Collapsed House":
            if not collapsed_house_searched:
                living_room_searched, bedroom_searched, rubble_pile_searched = collapsed_house(living_room_searched, bedroom_searched, rubble_pile_searched)
                collapsed_house_searched = True
            else:
                print("\n" *20)
                print("\nYou have already searched the Collapsed House.")
                living_room_searched, bedroom_searched, rubble_pile_searched = collapsed_house(living_room_searched, bedroom_searched, rubble_pile_searched)
        
        elif location == "Mansion":
            if not mansion_searched:
                (master_bedroom_searched, vault_searched, garden_searched, player_weapon_chosen, player_health, player_stamina, servant_defeated) = mansion(master_bedroom_searched, vault_searched, garden_searched, player_weapon_chosen, player_health, player_stamina, servant_defeated)
                mansion_searched = True
            else:
                print("\n" *20)
                print("\nYou have already searched the Mansion.")
                (master_bedroom_searched, vault_searched, garden_searched, player_weapon_chosen, player_health, player_stamina, servant_defeated) = mansion(master_bedroom_searched, vault_searched, garden_searched, player_weapon_chosen, player_health, player_stamina, servant_defeated)

        elif location == "Prison":
            if not prison_searched:
                kitchen_searched, cell_hallway_searched, cell_searched = prison(kitchen_searched, cell_hallway_searched, cell_searched)
                prison_searched = True
            else:
                print("\n" *20)
                print("\nYou have already searched the Prison.")
                kitchen_searched, cell_hallway_searched, cell_searched = prison(kitchen_searched, cell_hallway_searched, cell_searched)

        elif location == "School":
            school_key = "School Key"
            if school_key not in inventory["Keys"]:
                print("\n" *20)
                print("\nYou need the School Key to enter.")
            elif not school_searched:
                classroom_searched, school_library_searched, office_searched, cafeteria_searched = school(classroom_searched, school_library_searched, office_searched, cafeteria_searched)
                school_searched = True
            else:
                print("\n" *20)
                print("\nYou have already searched the School.")
                classroom_searched, school_library_searched, office_searched, cafeteria_searched = school(classroom_searched, school_library_searched, office_searched, cafeteria_searched)

        elif location == "Library":
            library_key = "Library Key"
            if library_key not in inventory["Keys"]:
                print("\n" *20)
                print("\nYou need the Library Key to enter.")
            elif not library_searched:
                bookshelf_searched, theatre_stage_searched, front_desk_searched = library(bookshelf_searched, theatre_stage_searched, front_desk_searched)
                library_searched = True
            else:
                print("\n" *20)
                print("\nYou have already entered the Library")
                bookshelf_searched, theatre_stage_searched, front_desk_searched = library(bookshelf_searched, theatre_stage_searched, front_desk_searched)

        elif location == "Train Station":
            train_station_key = "Train Station Key"
            if train_station_key not in inventory["Keys"]:
                print("\n" *20)
                print("\nYou need the Train Station Key to enter.")
            elif not train_station_searched:
                ticket_office_searched, boarding_area_searched = train_station(ticket_office_searched, boarding_area_searched)
                train_station_searched = True
            else:
                print("\n" *20)
                print("\nYou have already entered the Train Station")
                ticket_office_searched, boarding_area_searched = train_station(ticket_office_searched, boarding_area_searched)

        elif location == "Entrance Of The Mines":
            lever = "Lever"
            if lever not in inventory["Items"]:
                print("\n" *20)
                print("\nYou need a lever to enter")
            elif not entrance_of_the_mine_searched:
                cart_station_searched, railroad_searched, cart_on_rails, enter_mines = entrance_of_mine(cart_station_searched, railroad_searched, cart_on_rails)
                entrance_of_the_mines_searched = True
            else:
                print("\n" *20)
                print("\nYou have already visited the Entrance of the Mines.")
                cart_station_searched, railroad_searched, cart_on_rails, enter_mines = entrance_of_mine(cart_station_searched, railroad_searched, cart_on_rails)

                if enter_mines == True:
                    wires_needed = 3
                    battery_needed = "Battery"
                    wire_count = inventory["Items"].count("Wire")
                    has_battery = battery_needed in inventory["Items"]

                    if wire_count < wires_needed or not has_battery:
                        print("\n" *20)
                        print(f"\nYou need at least {wires_needed} Wires and a Battery to enter the Underground Railroad.")
                    elif not underground_railroad_searched:
                        wire_count, has_battery, miner_health, player_health, player_stamina, miner_defeated = underground_railroad(wire_count, has_battery, miner_health, miner_damage, player_health, player_stamina, player_weapon_chosen)
                        underground_railroad_searched = True
                    else:
                        print("\n" *20)
                        print("\nYou have already entered the Underground Railroad.")
                        wire_count, has_battery, miner_health, player_health, player_stamina, miner_defeated = underground_railroad(wire_count, has_battery, miner_health, player_health, player_stamina, player_weapon_chosen)

        elif location == "Underground Railroad":
            print("\n" *20)
            print("You cannot go into the Underground Railroad from here.")

        elif location.lower() in ["inventory", "inv", "i"]:
            show_inventory(player_weapon_chosen)
    
    replay = input("\n\n     - Yes     \n     - No \n\nWould you like to play again?").strip().lower()

    if replay in ["yes", "y"]:
        continue
    else:
        print("\n" *20)
        print("Thanks for playing!")
        break

