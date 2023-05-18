"""Version 2 of add combo, trialling a different way to ask the user for
their combo. Uses a new enter box for every item rather than a combined
multenterbox """

import easygui

# Stores monster cards in a nested dictionary
exist_cards = {"Stoneling":
                   {"Strength": 7, "Speed": 1, "Stealth": 25, "Cunning": 15},
               "Vexscream":
                   {"Strength": 1, "Speed": 6, "Stealth": 21, "Cunning": 19},
               "Dawnmirage":
                   {"Strength": 5, "Speed": 15, "Stealth": 18, "Cunning": 22},
               "Blazegolem":
                   {"Strength": 15, "Speed": 20, "Stealth": 23, "Cunning": 6},
               "Websnake":
                   {"Strength": 7, "Speed": 15, "Stealth": 10, "Cunning": 5},
               "Moldvine":
                   {"Strength": 21, "Speed": 18, "Stealth": 14, "Cunning": 5},
               "Vortexwing":
                   {"Strength": 19, "Speed": 13, "Stealth": 19, "Cunning": 2},
               "Rotthing":
                   {"Strength": 16, "Speed": 7, "Stealth": 4, "Cunning": 12},
               "Froststep":
                   {"Strength": 14, "Speed": 14, "Stealth": 7, "Cunning": 4},
               "Whispghoul":
                   {"Strength": 17, "Speed": 19, "Stealth": 3, "Cunning": 2},
               }

new_card = {}

# Get the values for each category
monster_name = easygui.enterbox(f"Enter the monster's name", "NAME")
strength = easygui.enterbox(f"Enter the value for 'Strength'", "STRENGTH")
speed = easygui.enterbox(f"Enter the value for 'Speed'", "SPEED")
stealth = easygui.enterbox(f"Enter the value for 'Stealth'", "STEALTH")
cunning = easygui.enterbox(f"Enter the value for 'Cunning'", "CUNNING")

# Add the user's card to a new dictionary

new_card[monster_name] = {}  # Adds key with monster name and empty dictionary
new_card[monster_name]["Strength"] = strength  # Adds strength
new_card[monster_name]["Speed"] = speed  # Adds speed
new_card[monster_name]["Stealth"] = stealth  # Adds stealth
new_card[monster_name]["Cunning"] = cunning  # Adds cunning

# Print the card and check with user that it is correct
card = ""
for monster_name, card_info in new_card.items():

    for category in card_info:
        card += f"{category}: {card_info[category]}\n"

easygui.buttonbox(f"Is the following card correct?\n\n"
                  f"{monster_name}\n\n"
                  f"{card}",
                  choices=["Yes", "No"])
