"""Version 3 of change card component, building on code from trial 1, adding
the blank checker function from component 2"""

import easygui


# Function to make sure input is entered and not left blank
def blank_checker(question, title, box):
    error_message = "You must fill out every field"

    if box == "enter":
        # Asks user for input
        answer = easygui.enterbox(question, title)

        while True:  # Loops until valid input is entered
            if answer == "":  # Checks if it is blank
                easygui.msgbox(error_message, "ERROR")  # Display error message
                answer = easygui.enterbox(question, title)

            if not answer:
                easygui.msgbox(error_message, "ERROR")  # Display error message
                answer = easygui.enterbox(question, title)
            else:
                return answer

    elif box == "integer":
        # Asks user for input
        answer = easygui.integerbox(question, title, lowerbound=1,
                                    upperbound=25)

        while True:  # Loops until valid input is entered
            if not answer:
                easygui.msgbox(error_message, "ERROR")  # Display error message
                answer = easygui.integerbox(question, title, lowerbound=1,
                                            upperbound=25)
            else:
                return answer

# Main Routine

# Card to change
new_card = {"STONELING":
                   {"Strength": 7, "Speed": 1, "Stealth": 25, "Cunning": 15}}

# Keep looping until the card is correct
while True:
    monster_name = ""

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
                                            " to?", "NAME", "enter").upper()
        # Replace the combo name with new name
        new_card[monster_name_change] = new_card.pop(monster_name)

    elif change == "Strength":

        # Ask user for new value
        new_strength = blank_checker("What would you like to change the value "
                                     "of 'Strength' to?", "STRENGTH",
                                     "integer")
        # Replace the current value with new one
        new_card[monster_name]["Strength"] = new_strength

    elif change == "Speed":

        # Ask user for new value
        new_speed = blank_checker("What would you like to change the value "
                                  "of 'Speed' to?", "SPEED", "integer")
        # Replace the current value with new one
        new_card[monster_name]["Speed"] = new_speed

    elif change == "Stealth":

        # Ask user for new value
        new_stealth = blank_checker("What would you like to change the value "
                                    "of 'Stealth' to?", "STEALTH", "integer")
        # Replace the current value with new one
        new_card[monster_name]["Stealth"] = new_stealth

    elif change == "Cunning":

        # Ask user for new value
        new_cunning = blank_checker("What would you like to change the value "
                                    "of 'Cunning' to?", "CUNNING", "integer")
        # Replace the current value with new one
        new_card[monster_name]["Cunning"] = new_cunning

