"""Version 1 of component 5 search card"""

import easygui

# Stores monster cards in a nested dictionary
exist_cards = {"STONELING":
                   {"Strength": 7, "Speed": 1, "Stealth": 25, "Cunning": 15},
               "VEXSCREAM":
                   {"Strength": 1, "Speed": 6, "Stealth": 21, "Cunning": 19},
               "DAWNMIRAGE":
                   {"Strength": 5, "Speed": 15, "Stealth": 18, "Cunning": 22},
               "BLAZEGOLELM":
                   {"Strength": 15, "Speed": 20, "Stealth": 23, "Cunning": 6},
               "WEBSNAKE":
                   {"Strength": 7, "Speed": 15, "Stealth": 10, "Cunning": 5},
               "MOLDVINE":
                   {"Strength": 21, "Speed": 18, "Stealth": 14, "Cunning": 5},
               "VORTEXWING":
                   {"Strength": 19, "Speed": 13, "Stealth": 19, "Cunning": 2},
               "ROTTHING":
                   {"Strength": 16, "Speed": 7, "Stealth": 4, "Cunning": 12},
               "FROSTSTEP":
                   {"Strength": 14, "Speed": 14, "Stealth": 7, "Cunning": 4},
               "WHISPGOUL":
                   {"Strength": 17, "Speed": 19, "Stealth": 3, "Cunning": 2}
               }

# Ask user to enter monster name they want to search
search_name = easygui.enterbox("Enter name of monster", "SEARCH").upper()

if search_name in exist_cards:
    easygui.msgbox(f"{search_name} is in the catalogue")

else:
    easygui.msgbox(f"Sorry, {search_name} is not in the catalogue")
