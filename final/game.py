# AC 2nd Final Project Text Adventure Game

import random

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

locations = ["Trailer Home", "Collapsed House", "Mansion", "Prison", "School", "Library", "Train Station", "Entrance of the Mine", "Underground Railroad"]

trailer_home_searched = False
collapsed_house_searched = False
mansion_searched = False
prison_searched = False
school_searched = False
library_searched = False
train_station_searched = False
entrance_of_the_mine_searched = False
underground_railroad_searched = False

player_health = 50
player_damage = random.randint(1, 10)
player_stamina = 10
player_weapon_chosen = "Dagger"

servant_health = 150
servant_damage = random.randint(1, 20)

miner_health = 250
miner_damage = random.randint(25, 50)

def intro_dialogue():
    print("\nYou heard of a rumor about an abandoned, small, ghost town 20 minutes away from your home town having valuable gems somewhere deep in the mines. No one has dared to go retrieve the valuable gems as there are spirits preventing you from going into the mines. Many deaths have been reported at this town.\n\nYou decide you want to go.\n\nYou inform your family and friends, they all try to stop you but you are determined.\n\nYou pack your bag with these items.\n\nDagger\nBandage\nEnergy Drink\nPhone\n\nYou set out and get to the town. Your adventure begins.\n\nYou arrive to the desolate town. Buildings are boarded up, the roads have a layer of sand and dirt, no one has stepped foot here in years. You take out your phone to call your family. The call rings infinitely, your phone has no service. It is just you, all alone.")

# Rooms

# Trailer Home
bathroom_searched = False
storage_cabinet_searched = False
main_area_searched = False

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

            elif search == "storage cabinet":
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

            elif search == "main area":
                if rubble_pile_searched == False:
                    rubble_pile_searched = True
                    rubble_pile_searched = True
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("\nYou see a suspicious looking rubble pile. You dig through and find an unlocked chest, and in this chest is a key labeled \"Library\"\n\n(+) Library Key")
                    inventory["Keys"]["Library Key"]
                    break
                elif rubble_pile_searched == True:
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("\nYou have already searched the bedroom and found the bandage.")
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

        

location = "Town"

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
            trailer_home(bathroom_searched, storage_cabinet_searched, main_area_searched)
            trailer_home_searched = True
        elif trailer_home_searched == True:
            print("You have already searched the Trailer Home")
            trailer_home(bathroom_searched = True, storage_cabinet_searched = True, main_area_searched = True)