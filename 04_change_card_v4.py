"""Version 4 of change card component, adding the blank checker function
from component 2"""

import easygui


# Function to make sure input is entered and not left blank
def blank_checker(question, title):
    error_message = "You must fill out every field"

    # Asks user for input
    answer = easygui.enterbox(question, title)

    while True:  # Loops until valid input is entered
        if answer == "":  # Checks if it is blank
            easygui.msgbox(error_message, "ERROR")  # Display error message
            answer = easygui.enterbox(question, title)
        else:
            return answer


# Main Routine

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
    change = easygui.buttonbox("What would you like to change?", "CATEGORIES",
                               choices=["Monster name", "Strength", "Speed",
                                        "Stealth", "Cunning"])

    if change == "Monster name":

        # Ask user for new combo name
        monster_name_change = blank_checker("What would you like to change it"
                                            " to?", "NAME",).upper()
        # Replace the combo name with new name
        new_card[monster_name_change] = new_card.pop(monster_name)

    elif change == "Strength":

        # Ask user for new value
        new_strength = easygui.integerbox("What would you like to change "
                                       "the value of 'Strength' to?",
                                       "STRENGTH", "", 1, 25)
        # Replace the current value with new one
        new_card[monster_name]["Strength"] = new_strength

    elif change == "Speed":

        # Ask user for new value
        new_speed = easygui.integerbox("What would you like to change the value"
                                       " of 'Speed' to?", "SPEED", "", 1, 25)
        # Replace the current value with new one
        new_card[monster_name]["Speed"] = new_speed

    elif change == "Stealth":

        # Ask user for new value
        new_stealth = easygui.integerbox("What would you like to change the "
                                         "value of 'Stealth' to?",
                                         "STEALTH", "", 1, 25)
        # Replace the current value with new one
        new_card[monster_name]["Stealth"] = new_stealth

    elif change == "Cunning":

        # Ask user for new value
        new_cunning = easygui.integerbox("What would you like to change the "
                                         "value of 'Cunning' to?", "CUNNING",
                                         "", 1, 25)
        # Replace the current value with new one
        new_card[monster_name]["Cunning"] = new_cunning

