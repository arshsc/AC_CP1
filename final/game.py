# AC 2nd Final Project Text Adventure Game

# import needed libraries
import random

# dictionary for the inventory
inventory = {
    "Weapons": {
        "Dagger": 10
    },
    "Consumables": {
        "Bandage": [10],  # +10 HP
        "Energy Drink": [4]  # +4 Stamina
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
locations = ["Trailer Home", "Collapsed House", "Mansion", "Prison", "School", "Library", "Train Station", "Entrance of the Mine", "Underground Railroad"]

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

# underground railroad
underground_railroad_searched = False


# combat
def servant_combat(player_health, player_stamina, player_weapon_chosen):

    ghost_health = 100
    base_player_damage = inventory["Weapons"][player_weapon_chosen]

    print("The servant ghost turns toward you.")
    print("\n\"YOU SHOULD NOT BE HERE,\" it yells.")

    print(f"\n Weapon Equipped: {player_weapon_chosen}(+{inventory['Weapons'][player_weapon_chosen]} DMG)")

    while True:
        fight_confirm = input("\n     - Yes\n     - No\n\nAre you sure you want to fight the ghost: ").strip().lower()
        if fight_confirm in ["yes", "y"]:
            print("\nYou steel yourself and step forward...")
            break
        elif fight_confirm in ["no", "n"]:
            print("\nYou take a step back, then turn around to run back into the mansion.")
            return player_health, player_stamina, False  # Cancel the fight
        else:
            print("Please type Yes or No.")

    # Randomly decide who goes first
    turn = random.randint(1, 2)

    while ghost_health > 0 and player_health > 0:

        if turn == 1:
            print("\nYOUR TURN")
            print(f"Your Health: {player_health}")
            print(f"Your Stamina: {player_stamina}")
            print(f"\nGhost Health: {ghost_health}")

            if player_stamina <= 0:
                print("\nYou are too exhausted to move!")
                player_stamina += 2
                print("You regain 2 stamina.")
                turn = 2
                continue

            choice = input("\n\n    - Quick Slash\n    - Charge Attack\n    - Consumable\n\nChoose an action: "
            ).lower().strip()

            if choice == "quick slash":
                damage = base_player_damage + 5
                player_stamina -= 1
                ghost_health -= damage
                print(f"\nYou dash forward and slash the ghost for {damage} damage!")

            elif choice == "charge attack":
                if player_stamina < 4:
                    print("\nYou don't have enough stamina!")
                    turn = 2
                    continue
                damage = base_player_damage + 10
                player_stamina -= 3
                ghost_health -= damage
                print(f"\nYou charge your weapon and strike for {damage} damage!")

            elif choice == "consumable":
                if len(inventory["Consumables"]["Bandage"]) == 0 and len(inventory["Consumables"]["Energy Drink"]) == 0:
                    print("\nYou have no consumables!")
                else:
                    use = input("\nUse Bandage or Energy Drink: ").lower().strip()

                    if use == "bandage" and len(inventory["Consumables"]["Bandage"]) > 0:
                        heal = inventory["Consumables"]["Bandage"].pop()
                        player_health += heal
                        if player_health > 50:
                            player_health = 50
                        print(f"\nYou heal yourself for {heal} HP.")

                    elif use == "energy drink" and len(inventory["Consumables"]["Energy Drink"]) > 0:
                        stam = inventory["Consumables"]["Energy Drink"].pop()
                        player_stamina += stam
                        print(f"\nYou regain {stam} stamina.")

                    else:
                        print("\nInvalid consumable choice.")

            else:
                print("\n" *20)
                print("\nInvalid action.")
                continue

            if ghost_health <= 0:
                print("\nThe servant lets out a final scream and fades away...")
                print("Something drops to the ground.")
                inventory["Items"].append("Servant Relic")
                print("\n(+) Servant Relic")
                return player_health, player_stamina, True

            turn = 2

        else:
            print("\nGHOST'S TURN")

            ghost_choice = random.randint(1, 2)

            if ghost_choice == 1:
                damage = random.randint(4, 7)
                print("\nThe servant slashes at you with icy claws!")
            else:
                damage = random.randint(8, 14)
                print("\nThe servant charges and smashes into you!")
            if random.randint(1, 100) <= 25:
                print("The servant’s attack passes through you!")
                damage = 0

            player_health -= damage
            print(f"You take {damage} damage!")

            # Check if player is dead
            if player_health <= 0:
                print("\nYour vision fades as the servant laughs...")
                print("YOU HAVE DIED.")
                return 0, player_stamina, False

            turn = 1
    if servant_health <= 0:
        print("\nThe ghost lets out a final wail and fades away...")
        print("You obtained the Ghost Servant's Item!")
        servant_defeated = True   # <-- important
        inventory["Weapons"]["Spectral Dagger"] = 30  # example drop
        return player_health, player_stamina, servant_defeated


# function for intro
def intro_dialogue():
    print("\nYou heard of a rumor about an abandoned, small, ghost town 20 minutes away from your home town having valuable gems somewhere deep in the mines. No one has dared to go retrieve the valuable gems as there are spirits preventing you from going into the mines. Many deaths have been reported at this town.\n\nYou decide you want to go.\n\nYou inform your family and friends, they all try to stop you but you are determined.\n\nYou pack your bag with these items.\n\nDagger\nBandage\nEnergy Drink\nPhone\n\nYou set out and get to the town. Your adventure begins.\n\nYou arrive to the desolate town. Buildings are boarded up, the roads have a layer of sand and dirt, no one has stepped foot here in years. You take out your phone to call your family. The call rings infinitely, your phone has no service. It is just you, all alone.")

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
                        print("\n\"WHAT NOTE SAYS!\"")
                        break
                    elif main_area_note in ["no", "n"]:
                        print("You put the note back down.")
                        break
                    else:
                        print("\nInvalid Option.")
                        continue
                elif main_area_searched == True:
                    print("\n" *20)
                    main_area_note = input("\nThere is nothing else here besides the note\n\n     - Yes     \n     - No \n\nWould you like to read the note again: ")
                    if main_area_note in ["yes", "y"]:
                        print("\n" *20)
                        print("\n\"WHAT NOTE SAYS!\"")
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

# mansion
def mansion(master_bedroom_searched, vault_searched, garden_searched, player_weapon_chosen, player_health, player_stamina):

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
                    inventory["Weapons"]["Ghost Axe"] = 50
                    while True:
                        print("\n" *20)
                        weapon_choice = input("     - Dagger (+10 DMG)\n     - Ghost Axe (+15 DMG)\nWhich weapon would you like to use?").strip().title()
                        if weapon_choice == "Dagger":
                            break
                        if weapon_choice == "Ghost Axe":
                            player_weapon_chosen = "Ghost Axe"
                            break
                    break
                elif vault_searched == True:
                    print("\n" *20)
                    print("\nYou have already searched the vault and found the Ghost Axe")
                    break

            elif search == "garden":
                if garden_searched == False:
                    garden_searched = True
                    if servant_defeated == False:
                        print("\n" *20)
                        print("\nYou walk to the back door and open the glass sliding door. A beautiful vibrant garden greets you. In the corner, you see a servant watering the flowers. He turns around and you see he is transparent. Its a ghost, and he seems to be angry at you.")
                        player_health, player_stamina, servant_defeated = servant_combat(player_health, player_stamina, player_weapon_chosen)
                        break
                    elif servant_defeated == True:
                        print("\n" *20)
                        print("\nThe servant has already been defeated. The garden is peaceful now.")
                elif garden_searched == True:
                    print("\n" *20)
                    print("\nYou have already fought the servant and got the...ITEM")
                    break

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
                    office_note = input("\nYou can't enter the office as it is locked shut. you peek over the front desk and find a note.\n\n     - Yes     \n     - No \n\nWould you like to read it: ").strip().lower()
                    if office_note in ["yes", "y"]:
                        print("\n" *20)
                        print("\n\"WHAT NOTE SAYS!\"")
                        break
                    elif office_note in ["no", "n"]:
                        print("You put the note back down.")
                        break
                elif office_searched == True:
                    office_note = input("\nThere is nothing else here besides the note. Would you like to read the note again: ")
                    while True:
                        if office_note in ["yes", "y"]:
                            print("\n" *20)
                            print("\n\"WHAT NOTE SAYS!\"")
                            break
                        elif office_note in ["no", "n"]:
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

# library
def library(bookshelf_searched, theatre_stage, front_desk_searched):

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
                if theatre_stage == False:
                    theatre_stage = True
                    print("\n" *20)
                    print("\nYou walk over the the theatre stage. the floorboards are cracked with some missing. You see a dangling wire on the right and decide to take it.\n\n(+) Wire")
                    inventory["Items"].append("Wire")
                    break
                elif theatre_stage == True:
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

# entrance of mine
def entrance_of_mine(cart_station_searched, railroad_searched):

    location = "Entrance of the Mines"
    cart_on_rails = False
    
    print("\n" *20)
    print("You walk to the entrance of the mines. The lever to open the gate is broken. You pull it off and insert the lever you stored in your backpack. You flick the lever and the gate opens.")
    print("\nThere is a narrow hallway leading to the railroad with a few carts on the sides.")

    while location == "Train Station":

        while True:
            search = input("\nThere are 2 areas worth searching.\n   \n     - Cart Station   \n     - Railroad   \n     - Exit\n\nWhere would you like to go: ").lower().strip()

            if search in ["cart station", "railroad", "exit"]:
                break
            else:
                print("\nThat is not a room, please retry.")

        while True:
            if search == "cart station":
                if cart_station_searched == False:
                    cart_station_searched = True
                    print("\n" *20)
                    print("\nYou turn the corner to the cart station. A bunch of old carts are left here. You need one to go down into the mines. So you decide to grab a cart and put it onto the rails.")
                    cart_on_rails = True
                    break
                elif cart_station_searched == True:
                    print("\n" *20)
                    print("\nYou already searched the cart station and put the cart on to the rails.")
                    break

            elif search == "railroad":
                if railroad_searched == False:
                    railroad_searched = True
                    if cart_on_rails == False:
                        print("\n" *20)
                        print("\nYou walk to the rails and see it goes into a dark tunnel. You don't have a cart to go in.")
                        break
                    elif cart_on_rails == True:
                        print("\n" *20)
                        go_into_mines = input("\nYou are ready to go down into the mines\n\n     - Yes\n     - No\nWould you like to:")
                        return go_into_mines
                elif railroad_searched == True:
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
# room input and inventory function
def room_input(locations):
    while True:
        print("\nThese locations look worth exploring.\n")

        for l in locations:
            print(f"     - {l}")
        print("\nTo see what is in your backpack")
        print("\n     - Inventory")

        choice = input("\nWhat building would you like to go to: ").title().strip()

        if choice.lower() in ["inventory", "inv", "i"]:
            print("\n" *20)
            show_inventory()
            continue

        if choice not in locations:
            print("\n" *20)
            print("\nThat place doesn't exist, choose another place.")
            continue

        return choice

# inventory
def show_inventory(player_weapon_chosen):
    print(f"Weapon in use: {player_weapon_chosen}")
    print("\nWeapons:")
    for weapon, dmg in inventory["Weapons"].items():
        print(f" - {weapon}: {dmg} dmg")

    print("\nConsumables:")
    for item, effects in inventory["Consumables"].items():
        for effect in effects:
            if item == "Bandage":
                print(f" - {item}: +{effect} HP")
            elif item == "Energy Drink":
                print(f" - {item}: +{effect} Stamina")

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

intro_dialogue()

while True:

    location = room_input(locations)

    if location == "Trailer Home":
        if not trailer_home_searched:
            trailer_home(bathroom_searched, storage_cabinet_searched, main_area_searched)
            trailer_home_searched = True
        else:
            print("\n" *20)
            print("\nYou have already searched the Trailer Home.")
            trailer_home(bathroom_searched = True, storage_cabinet_searched = True, main_area_searched = True)

    elif location == "Collapsed House":
        if not collapsed_house_searched:
            collapsed_house(living_room_searched, bedroom_searched, rubble_pile_searched)
            collapsed_house_searched = True
        else:
            print("\n" *20)
            print("\nYou have already searched the Collapsed House.")
            collapsed_house(living_room_searched = True, bedroom_searched = True, rubble_pile_searched = True)
    
    elif location == "Mansion":
        if not mansion_searched:
            mansion(master_bedroom_searched, vault_searched, garden_searched, player_weapon_chosen, player_health, player_stamina)
            mansion_searched = True
        else:
            print("\n" *20)
            print("\nYou have already searched the Mansion.")
            collapsed_house(living_room_searched = True, bedroom_searched = True, rubble_pile_searched = True, weapon = player_weapon_chosen)

    elif location == "Prison":
        if not prison_searched:
            prison(kitchen_searched, cell_hallway_searched, cell_searched)
            prison_searched = True
        else:
            print("\n" *20)
            print("\nYou have already searched the Prison.")
            prison(kitchen_searched = True, cell_hallway_searched = True, cell_searched = True)

    elif location == "School":
        school_key = "School Key"
        if school_key not in inventory["Keys"]:
            print("\n" *20)
            print("\nYou need the School Key to enter.")
        elif not school_searched:
            school(classroom_searched, school_library_searched, office_searched, cafeteria_searched)
            school_searched = True
        else:
            print("\n" *20)
            print("\nYou have already searched the School.")
            school(classroom_searched = True, school_library_searched = True, office_searched = True, cafeteria_searched = True)

    elif location == "Library":
        library_key = "Library Key"
        if library_key not in inventory["Keys"]:
            print("\n" *20)
            print("\nYou need the Library Key to enter.")
        elif not library_searched:
            library(bookshelf_searched, theatre_stage_searched, front_desk_searched)
            library_searched = True
        else:
            print("\n" *20)
            print("\nYou have already entered the Library")
            library(bookshelf_searched =  True, theatre_stage_searched = True, front_desk_searched = True)

    elif location == "Train Station":
        train_station_key = "Train Station Key"
        if train_station_key not in inventory["Keys"]:
            print("\n" *20)
            print("\nYou need the Train Station Key to enter.")
        elif not train_station_searched:
            train_station(ticket_office_searched, boarding_area_searched)
            train_station_searched = True
        else:
            print("\n" *20)
            print("\nYou have already entered the Train Station")
            train_station(ticket_office_searched = True, boarding_area_searched = True)

    elif location.lower() in ["inventory", "inv", "i"]:
        show_inventory(player_weapon_chosen)


