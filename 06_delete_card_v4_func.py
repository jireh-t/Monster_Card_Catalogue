"""Builds on the code from version 3, and turns it into a function to use
later"""

import easygui


# Function to delete a card
def delete_card(cards):

    # List to append the monster names to
    choices = []

    # Loop to print all cards in catalogue
    for monster_name in exist_cards:
        choices.append(monster_name)

    # Ask the user what card they want to delete
    card_del = easygui.choicebox("Select the card you would like to delete",
                                 "DELETE", choices)

    # Ask user to confirm decision
    sure = easygui.buttonbox(
        f"Are you sure you want to delete {card_del} from the "
        f"catalogue?\n\n"
        f"This cannot be undone",
        "PLEASE CONFIRM",
        choices=["Yes", "No"])

    if sure == "Yes":
        # Delete the card
        del [cards[card_del]]
        easygui.msgbox(f"{card_del} has been deleted", "DELETED")


# Main Routine

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

delete_card(exist_cards)
print(exist_cards)
