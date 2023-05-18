"""Component 2 Add combo version 1
This code will be trial 1 using an enterbox with multiple fields to get the
user's combo"""

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

# Get the values of the cards

text = "Enter the following values of your card"  # Prompt for user to type
title = "ENTER CARD"  # Title shown

# Fields to fill in
input_list = ["Monster name", "Strength", "Speed", "Stealth", "Cunning"]

# User's inputs are added to a list
values = easygui.multenterbox(text, title, input_list)

# Add the user's card to a new dictionary

new_card[values[0]] = {}  # Adds key with monster name and empty dictionary
new_card[values[0]]["Strength"] = values[1]  # Adds strength
new_card[values[0]]["Speed"] = values[2]  # Adds speed
new_card[values[0]]["Stealth"] = values[3]  # Adds stealth
new_card[values[0]]["Cunning"] = values[4]  # Adds cunning

# Print the card and check with user that it is correct
card = ""
for monster_name, card_info in new_card.items():

    for category in card_info:
        card += f"{category}: {card_info[category]}\n"

easygui.buttonbox(f"Is the following card correct?\n\n"
                  f"{monster_name}\n\n"
                  f"{card}",
                  choices=["Yes", "No"])

