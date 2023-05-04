"""Trial 1 of change card, this will trial the user selecting what specific
category they would like to change"""

import easygui

# Card to change
new_card = {"STONELING":
                   {"Strength": 7, "Speed": 1, "Stealth": 25, "Cunning": 15}}

# Keep looping until the card is correct
while True:

    # Print the card and check with user that it is correct
    card = ""
    for monster_name, card_info in new_card.items():

        for category in card_info:
            card += f"{category}: {card_info[category]}\n"

    choice = easygui.buttonbox(f"Is the following card correct?\n\n"
                               f"{monster_name}\n\n"
                               f"{card}", "CONFIRM",
                               choices=["Yes", "No"])

    if choice == "Yes":
        break

    # Ask the user what they would like to change
    change = easygui.buttonbox("What would you like to change?",
                               choices=["Monster name", "Strength", "Speed",
                                        "Stealth", "Cunning"])

    if change == "Monster name":

        # Ask user for new combo name
        monster_name_change = easygui.enterbox("What would you like to change "
                                               "it to?").upper()
        # Replace the combo name with new name
        new_card[monster_name_change] = new_card.pop(monster_name)

    elif change == "Strength":

        # Ask user for new value
        new_strength = easygui.enterbox(f"What would you like to change the "
                                        f"value of 'Strength' to?")

        # Replace the current value with new one
        new_card[monster_name]["Strength"] = new_strength

    elif change == "Speed":

        # Ask user for new value
        new_speed = easygui.enterbox(f"What would you like to change the "
                                     f"value of 'Speed' to?")

        # Replace the current value with new one
        new_card[monster_name]["Speed"] = new_speed

    elif change == "Stealth":

        # Ask user for new value
        new_stealth = easygui.enterbox(f"What would you like to change the "
                                       f"value of 'Stealth' to?")

        # Replace the current value with new one
        new_card[monster_name]["Stealth"] = new_stealth

    elif change == "Cunning":

        # Ask user for new value
        new_cunning = easygui.enterbox(f"What would you like to change the "
                                       f"value of 'Cunning' to?")

        # Replace the current value with new one
        new_card[monster_name]["Cunning"] = new_cunning

