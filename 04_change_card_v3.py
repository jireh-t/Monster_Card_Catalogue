"""Version 3 of change card component, making the enter boxes integer boxes"""

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
        monster_name_change = easygui.integerbox("What would you like to "
                                                 "change it to?", "", 1, 25
                                                 ).upper()
        # Replace the combo name with new name
        new_card[monster_name_change] = new_card.pop(monster_name)

    elif change == "Strength":

        # Ask user for new value
        new_strength = easygui.integer("What would you like to change "
                                       "the value of 'Strength' to?", "", 1,
                                       25)
        # Replace the current value with new one
        new_card[monster_name]["Strength"] = new_strength

    elif change == "Speed":

        # Ask user for new value
        new_speed = easygui.integerbox("What would you like to change the value"
                                       " of 'Speed' to?", "", 1, 25)
        # Replace the current value with new one
        new_card[monster_name]["Speed"] = new_speed

    elif change == "Stealth":

        # Ask user for new value
        new_stealth = easygui.integerbox("What would you like to change the "
                                         "value of 'Stealth' to?", "", 1, 25)
        # Replace the current value with new one
        new_card[monster_name]["Stealth"] = new_stealth

    elif change == "Cunning":

        # Ask user for new value
        new_cunning = easygui.integerbox("What would you like to change the "
                                         "value of 'Cunning' to?", "", 1, 25)
        # Replace the current value with new one
        new_card[monster_name]["Cunning"] = new_cunning

