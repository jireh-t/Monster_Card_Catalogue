"""Version 2 of add combo, adds the blank checker function from component 2"""

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

new_card = {}

# Get the values for each category
monster_name = blank_checker("Enter the monster's name", "NAME",
                             "enter").upper()
strength = blank_checker("Enter the value for 'Strength'", "STRENGTH",
                         "integer")
speed = blank_checker("Enter the value for 'Speed'", "SPEED", "integer")
stealth = blank_checker("Enter the value for 'Stealth'", "STEALTH", "integer")
cunning = blank_checker("Enter the value for 'Cunning'", "CUNNING", "integer")

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
                  f"{card}", "CONFIRM",
                  choices=["Yes", "No"])
