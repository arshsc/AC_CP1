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
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("You walk over towards the trailer home. The door is unlocked and you walk in.")
    print("\nThis is a very small trailer home. The walls are yellow with dirt scattered all throughout the inside.")

    while True:

        while True:
            search = input("\nThere are 3 areas worth searching.\n   \n-Bathroom   \n-Storage Cabinet   \n-Main Area\n\nWhere would you like to search: ").lower().strip()

            if search == "bathroom" or "storage cabinet" or "main area":
                break
            else:
                print("\nThat is not a room, please retry.")

        while True:
            if search == "bathroom":
                if bathroom_searched == False:
                    bathroom_searched = True
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("\nYou enter the cramped bathroom. Near the sink, there is a bandage. You pick it up and put it in your backpack. Nothing else is in here and you exit.")
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
                    print("\nYou open the big storage cabinet. Old clothes and jackets scatter the insides. You dig through the old clothes and find a key with an engraving that says \"School Front Door\". You stash it in your backpack.")
                    break
                elif storage_cabinet_searched == True:
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("\nYou have already searched the storage cabinet and found a key engraved with \"School Front Door\".")
                    break

            elif search == "main area":
                if main_area_searched == False:
                    main_area_searched = True
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    bathroom_note = input("\nYou look around your surroundings. On the small dining table there is a note available to read.\n     Yes\n     No Would you like to read it: ").strip().lower()
                    if bathroom_note == "yes" or "y":
                        print("\n\"WHAT NOTE SAYS!\"")
                        break
                    elif bathroom_note == "no" or "n":
                        print("You put the note back down.")
                        break
                elif main_area_searched == True:
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    bathroom_note = input("\nThere is nothing else here besides the note. Would you like to read the note again: ")
                    while True:
                        if bathroom_note == "yes" or "y":
                            print("\n\"WHAT NOTE SAYS!\"")
                            break
                        elif bathroom_note == "no" or "n":
                            break

        


def room_input(locations):

    global trailer_home_searched

    print("\nThese locations look worth exploring.\n")

    for l in locations:
        print(f"- {l}")
    while True:
        location = input("\nWhere would you like to go: ").title()
        if location not in locations:
            print("\nThat place doesn't exist, choose another place.")
            continue
        elif location == "Trailer Home":
            trailer_home(bathroom_searched, storage_cabinet_searched, main_area_searched)
            trailer_home_searched = True
        else:
            return location

intro_dialogue()
location = room_input(locations)
print(location)