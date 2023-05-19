"""Trial 1 of delete card to show the user the full list of cards and then
ask them to enter the card to delete"""

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

catalogue = ""

# Loop to print all cards in catalogue
for monster_name in exist_cards:

    # Print the monster name
    catalogue += f"\n{monster_name}\n"


# Output the full catalogue and ask the user what card to delete
choice = easygui.enterbox(f"/ / / Below is all the cards in the catalogue/ / "
                          f"/\n\n"
                          f"{catalogue}\n\n"
                          "Which card would you like to delete?").upper()

# Show error message if the card is not in the catalogue

while choice not in exist_cards:
    easygui.msgbox(f"Sorry, {choice} is not in the catalogue", "ERROR")

    # Output the full catalogue and ask the user what card to delete
    choice = easygui.enterbox(f"/ / / Below is all the cards in the catalogue/ / "
                              f"/\n\n"
                              f"{catalogue}\n\n"
                              "Which card would you like to delete?",
                              "ENTER MONSTER NAME").upper()

# Delete the card
del[exist_cards[choice]]
easygui.msgbox(f"{choice} has been deleted", "DELETED")
