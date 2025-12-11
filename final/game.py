# AC 2nd Final Project Text Adventure Game

# import needed libraries
import random

# dictionary for the inventory
inventory = {
    "Weapons": {
        "Dagger": 10
    },
    "Consumables": {
        "Bandage": 10,
        "Energy Drink": 5
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

# underground railraod
underground_railroad_searched = False


# function for intro
def intro_dialogue():
    print("\nYou heard of a rumor about an abandoned, small, ghost town 20 minutes away from your home town having valuable gems somewhere deep in the mines. No one has dared to go retrieve the valuable gems as there are spirits preventing you from going into the mines. Many deaths have been reported at this town.\n\nYou decide you want to go.\n\nYou inform your family and friends, they all try to stop you but you are determined.\n\nYou pack your bag with these items.\n\nDagger\nBandage\nEnergy Drink\nPhone\n\nYou set out and get to the town. Your adventure begins.\n\nYou arrive to the desolate town. Buildings are boarded up, the roads have a layer of sand and dirt, no one has stepped foot here in years. You take out your phone to call your family. The call rings infinitely, your phone has no service. It is just you, all alone.")


# trailer home
def trailer_home(bathroom_searched, storage_cabinet_searched, main_area_searched):

    location = "Trailer Home"
    
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("You walk over towards the trailer home. The door is unlocked and you walk in.")
    print("\nThis is a very small trailer home. The walls are yellow with dirt scattered all throughout the inside.")

    while location == "Trailer Home":

        while True:
            search = input("\nThere are 3 areas worth searching.\n   \n     - Bathroom   \n     - Storage Cabinet   \n     - Main Area     \n     - Exit\n\nWhere would you like to go: ").lower().strip()

            if search == "bathroom" or "storage cabinet" or "main area" or "exit":
                break
            else:
                print("\nThat is not a room, please retry.")

        while True:
            if search == "bathroom":
                if bathroom_searched == False:
                    bathroom_searched = True
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("\nYou enter the cramped bathroom. Near the sink, there is a bandage. You pick it up and put it in your backpack. Nothing else is in here and you exit.\n\n(+) Bandage")
                    inventory["Consumables"]["Bandage"] = 10
                    break
                elif bathroom_searched == True:
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("\nYou already searched the bathroom, you picked up the bandage and nothing else is to be found.")
                    break

            elif search == "storage cabinet":
                if storage_cabinet_searched == False:
                    storage_cabinet_searched = True
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("\nYou open the big storage cabinet. Old clothes and jackets scatter the insides. You dig through the old clothes and find a key with an engraving that says \"School Front Door\". You stash it in your backpack.\n\n(+) School Front Door Key")
                    inventory["Keys"].append("School Key")
                    break
                elif storage_cabinet_searched == True:
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("\nYou have already searched the storage cabinet and found a key engraved with \"School Front Door\".")
                    break

            elif search == "main area":
                if main_area_searched == False:
                    main_area_searched = True
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    main_area_note = input("\nYou look around your surroundings. On the small dining table there is a note available to read.\n\n     - Yes     \n     - No \n\nWould you like to read it: ").strip().lower()
                    if main_area_note == "yes" or "y":
                        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                        print("\n\"WHAT NOTE SAYS!\"")
                        break
                    elif main_area_note == "no" or "n":
                        print("You put the note back down.")
                        break
                elif main_area_searched == True:
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    main_area_note = input("\nThere is nothing else here besides the note. Would you like to read the note again: ")
                    while True:
                        if main_area_note == "yes" or "y":
                            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                            print("\n\"WHAT NOTE SAYS!\"")
                            break
                        elif main_area_note == "no" or "n":
                            break

            elif search == "exit":
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print("\nYou exit the trailer home")
                location = "Town"
                break

            else:
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print("\nThat is not a valid option, please retry.")
                break

# collapsed house
def collapsed_house(living_room_searched, bedroom_searched, rubble_pile_searched):

    location = "Collapsed House"
    
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("You walk over towards the collapsed house. The door is unlocked and you walk in.")
    print("\nAll that is left is a few standing wall. The roof has caved in.")

    while location == "Collapsed House":

        while True:
            search = input("\nThere are 3 areas worth searching.\n   \n     - Living Room   \n     - Bedroom   \n     - Rubble Pile     \n     - Exit\n\nWhere would you like to go: ").lower().strip()

            if search == "living room" or "bedroom" or "rubble pile" or "exit":
                break
            else:
                print("\nThat is not a room, please retry.")

        while True:
            if search == "living room":
                if living_room_searched == False:
                    living_room_searched = True
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("\nYou enter the wide living room. There is not much here besides a table and a few couches covered in rubble. Nothing is found here worth to take.")
                    break
                elif living_room_searched == True:
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("\nYou already searched the living room, nothing was here to be found.")
                    break

            elif search == "bedroom":
                if bedroom_searched == False:
                    bedroom_searched = True
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("\nYou walk into a lone doorway with no wall, this seems to be the master bedroom of the house. You see a dresser barely visible from all the rubble. You walk to it, dig to the dresser drawer and inside you find a bandage.\n\n(+) Bandage")
                    inventory["Consumables"]["Bandage"] = 10
                    break
                elif bedroom_searched == True:
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("\nYou have already searched the bedroom and found the bandage.")
                    break

            elif search == "rubble pile":
                if rubble_pile_searched == False:
                    rubble_pile_searched = True
                    rubble_pile_searched = True
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("\nYou see a suspicious looking rubble pile. You dig through and find an unlocked chest, and in this chest is a key labeled \"Library\"\n\n(+) Library Key")
                    inventory["Keys"].append("Library Key")
                    break
                elif rubble_pile_searched == True:
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("\nYou have already searched the rubble pile and found the library key.")
                    break

            elif search == "exit":
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print("\nYou exit the collapsed house")
                location = "Town"
                break

            else:
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print("\nThat is not a valid option, please retry.")
                break

# mansion
def mansion(master_bedroom_searched, vault_searched, garden_searched):

    location = "Mansion"
    
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("You walk over towards the mansion. The door is unlocked and you walk in.")
    print("\nThis house is huge. An endless hallway greets you, but most of the hallway seems to be blocked.")

    while location == "Mansion":

        while True:
            search = input("\nThere are 3 areas worth searching.\n   \n     - Master Bedroom   \n     - Vault   \n     - Garden     \n     - Exit\n\nWhere would you like to go: ").lower().strip()

            if search == "master bedroom" or "vault" or "garden" or "exit":
                break
            else:
                print("\nThat is not a room, please retry.")

        while True:
            if search == "master bedroom":
                if master_bedroom_searched == False:
                    master_bedroom_searched = True
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("\nYou enter the massive bedroom. There is elegant furniture throughout the whole room. You open the nightstand and find a key labeled \"Train Station\".\n\n(+) Train Station Key")
                    inventory["Keys"].append("Train Station Key")
                    break
                elif master_bedroom_searched == True:
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("\nYou already searched the master bedroom, you picked up the \"Train Station\" and nothing else is to be found.")
                    break

            elif search == "vault":
                if vault_searched == False:
                    vault_searched = True
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("\nYou walk down the grand stairs into the basement. The only thing in this basement is a giant vault door, slightly cracked open. You peek in and see an intact glass showcase with an axe. This is not an ordinary axe, it has a mysterious dark aura around it. You pick it up and feel an eerie feeling.\n\n(+) Ghost Axe")
                    inventory["Weapons"].append("Ghost Axe")
                    break
                elif vault_searched == True:
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("\nYou have already searched the vault and found a the Ghost Axe")
                    break

            elif search == "garden":
                if garden_searched == False:
                    garden_searched = True
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("\nYou walk to the back door and open the glass sliding door. A beautiful vibrant garden greets you. In the corner, you see a servant watering the flowers. He turns around and you see he is transparent. Its a ghost, and he seems to be angry at you.")
                    break
                elif garden_searched == True:
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("\nYou have already fought the servant and got the...ITEM")
                    break

            elif search == "exit":
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print("\nYou exit the Mansion")
                location = "Town"
                break

            else:
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print("\nThat is not a valid option, please retry.")
                break
        
# prison
def prison(kitchen_searched, cell_hallway_searched, cell_searched):

    location = "Prison"
    
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("You walk over towards the massive prison gates. The door is locked but it seems easy to climb, so you do so and get in.")
    print("\nThis prison is huge. A lot of it is boarded up and not too many rooms are available.")

    while location == "Prison":

        while True:
            search = input("\nThere are 3 areas worth searching.\n   \n     - Kitchen   \n     - Cell Hallway   \n     - Cell     \n     - Exit\n\nWhere would you like to go: ").lower().strip()

            if search == "kitchen" or "cell hallway" or "cell" or "exit":
                break
            else:
                print("\nThat is not a room, please retry.")

        while True:
            if search == "kitchen":
                if kitchen_searched == False:
                    kitchen_searched = True
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("\nYou enter the kitchen. It is filthy, but some food could be nice. You open the storage room and see a bunch of food. You pick some up and realize they all expired decades ago.\n\n")
                    break
                elif kitchen_searched == True:
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("\nYou already searched the kitchen. Nothing was to be found")
                    break

            elif search == "cell hallway":
                if cell_hallway_searched == False:
                    cell_hallway_searched = True
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("\nYou walk to the massive hallway. Cells on each side with a second story of more cells. On the side near the emergency exit, there seems to be some sort of battery. You pick it up.\n\n(+) Battery")
                    inventory["Items"].append("Battery")
                    break
                elif cell_hallway_searched == True:
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("\nYou have already searched the cell hallway and found a battery.")
                    break

            elif search == "cell":
                if cell_searched == False:
                    cell_searched = True
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("\nYou walk into one of the only cells not blocked. You search the small table and under the bed. You find a single wire under the bed. \n\n(+) Wire")
                    inventory["Items"].append("Wire")
                    break
                elif cell_searched == True:
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("\nYou have already searched the cell and found a wire.")
                    break

            elif search == "exit":
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print("\nYou exit the Prison")
                location = "Town"
                break

            else:
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print("\nThat is not a valid option, please retry.")
                break

# school
def school(classroom_searched, school_library_searched, office_searched, cafeteria_searched):

    location = "School"
    
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("You walk over towards the school. You use your school key and it works, the front door opens.")
    print("\nThis is a relatively small and very old school.")

    while location == "School":

        while True:
            search = input("\nThere are 4 areas worth searching.\n   \n     - Classroom   \n     - School Library   \n     - Office     \n     - Cafeteria     \n     - Exit\n\nWhere would you like to go: ").lower().strip()

            if search == "classroom" or "school library" or "office" or "cafeteria" or "exit":
                break
            else:
                print("\nThat is not a room, please retry.")

        while True:

            if search == "classroom":
                if classroom_searched == False:
                    classroom_searched = True
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("\nYou enter the classroom. The roof seems that it is about to cave in. On one of the desks, there is an unopened energy drink that seems new. You pick it up and put it in your backpack.\n\n(+) Bandage")
                    inventory["Consumables"]["Energy Drink"] = 4
                    break
                elif classroom_searched == True:
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("\nYou already searched the classroom, you picked up the energy drink and nothing else is to be found.")
                    break

            elif search == "school library":
                if school_library_searched == False:
                    school_library_searched = True
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("\You walk into the tiny library. The bookshelves are on the floor, and many books scattered through the floor. Nothing useful seems to be in here.")
                    break
                elif school_library_searched == True:
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("\nYou have already searched the library and nothing was to be found.")
                    break

            elif search == "office":
                if office_searched == False:
                    office_searched = True
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    office_note = input("\nYou can't enter the office as it is locked shut. you peek over the front desk and find a note.\n\n     - Yes     \n     - No \n\nWould you like to read it: ").strip().lower()
                    if office_note == "yes" or "y":
                        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                        print("\n\"WHAT NOTE SAYS!\"")
                        break
                    elif office_note == "no" or "n":
                        print("You put the note back down.")
                        break
                elif office_searched == True:
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    office_note = input("\nThere is nothing else here besides the note. Would you like to read the note again: ")
                    while True:
                        if office_note == "yes" or "y":
                            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                            print("\n\"WHAT NOTE SAYS!\"")
                            break
                        elif office_note == "no" or "n":
                            break

            elif search == "exit":
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print("\nYou exit the school")
                location = "Town"
                break

            else:
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print("\nThat is not a valid option, please retry.")
                break

def room_input(locations, inventory):

    while True:
        print("\nThese locations look worth exploring.\n")

        for l in locations:
            print(f"     - {l}")
        print("\nTo see what is in your backpack")
        print("\n     - Inventory")

        location = input("\nWhat building would you like to go to: ").title().strip()

        """if location == "inventory" or "inv" or "i":
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            for key, item, in inventory.items():
                print(f"{key}: {item}")
            continue"""

        if location not in locations:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("\nThat place doesn't exist, choose another place.")
            continue

        elif location in location:
            return location

        
    
intro_dialogue()

while True:
    location = room_input(locations, inventory)

    if location == "Trailer Home":
        if trailer_home_searched == False:
            trailer_home(bathroom_searched, storage_cabinet_searched,  main_area_searched)
            trailer_home_searched = True
        elif trailer_home_searched == True:
            print("\nYou have already searched the Trailer Home.")
            trailer_home(bathroom_searched = True, storage_cabinet_searched = True, main_area_searched = True)

    elif location == "Collapsed House":
        if collapsed_house_searched == False:
            collapsed_house(living_room_searched, bedroom_searched, rubble_pile_searched)
            collapsed_house_searched = True
        elif collapsed_house_searched == True:
            print("\nYou have already searched the Collapsed House.")
            collapsed_house(living_room_searched = True, bedroom_searched = True, rubble_pile_searched = True)
    
    elif location == "Mansion":
        if mansion_searched == False:
            mansion(living_room_searched, bedroom_searched, rubble_pile_searched)
            mansion_searched = True
        elif mansion_searched == True:
            print("\nYou have already searched the Mansion.")
            mansion(master_bedroom_searched = True, vault_searched = True, garden_searched = True)

    elif location == "Prison":
        if prison_searched == False:
            prison(kitchen_searched, cell_hallway_searched, cell_hallway_searched)
            prison_searched = True
        elif prison_searched == False:
            print("\nYou have already searched the Prison")
            prison(kitchen_searched = True, cell_hallway_searched = True, cell_searched = True)

    elif location == "School":
        school_key = "School"
        if school_searched == False:
            if school_key in inventory["Keys"]:
                school()