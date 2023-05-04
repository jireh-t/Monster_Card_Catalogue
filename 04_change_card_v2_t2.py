"""Trial 2 of change combo component, if the combo is incorrect the entering
process restarts"""

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

while True:
    new_card = {}

    # Get the values for each category
    monster_name = blank_checker("Enter the monster's name", "NAME",).upper()
    strength = easygui.integerbox("Enter the value for 'Strength'", "STRENGTH",
                                  "", 1, 25)
    speed = easygui.integerbox("Enter the value for 'Speed'", "SPEED", "", 1, 25)
    stealth = easygui.integerbox("Enter the value for 'Stealth'", "STEALTH",
                                 "", 1, 25)
    cunning = easygui.integerbox("Enter the value for 'Cunning'", "CUNNING",
                                 "", 1, 25)

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

    choice = easygui.buttonbox(f"Is the following card correct?\n\n"
                               f"{monster_name}\n\n"
                               f"{card}", "CONFIRM",
                               choices=["Yes", "No"])

    # If card is correct then stop
    if choice == "Yes":
        break

    # If incorrect, restart the process
    else:
        easygui.msgbox("Sorry please try again")
