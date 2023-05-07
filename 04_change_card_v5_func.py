"""Version 5 of change card component, making the previous code more
flexible by putting it into a function"""

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


# Function to allow user to edit the combo
def change_card(card_confirm):

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

        # When user is happy with the card

        if choice == "Yes":
            easygui.msgbox(f"You have successfully confirmed the card "
                           f"{monster_name}", "CARD CONFIRMED")
            return card_confirm

        # Ask the user what they would like to change
        change = easygui.buttonbox("What would you like to change?",
                                   "CATEGORIES",
                                   choices=["Monster name", "Strength",
                                            "Speed", "Stealth", "Cunning"])

        if change == "Monster name":

            # Ask user for new combo name
            monster_name_change = blank_checker("What would you like to "
                                                "change it to?",
                                                "NAME",).upper()

            # If the name has already been used
            while monster_name_change in exist_cards:  # Fix when user wants
                # to change back??

                # Error message
                easygui.msgbox(f"{monster_name_change} is already the "
                               f"name of a monster card in the deck\n You "
                               f"must choose a different name",
                               "ERROR")

                # Ask user for new combo name
                monster_name_change = blank_checker("What would you like to "
                                                    "change it to?",
                                                    "NAME",).upper()

            # Replace the combo name with new name
            card_confirm[monster_name_change] = new_card.pop(monster_name)

        elif change == "Strength":

            # Ask user for new value
            new_strength = easygui.integerbox("What would you like to change "
                                              "the value of 'Strength' to?",
                                              "STRENGTH", "", 1, 25)
            # Replace the current value with new one
            card_confirm[monster_name]["Strength"] = new_strength

        elif change == "Speed":

            # Ask user for new value
            new_speed = easygui.integerbox("What would you like to change "
                                           "the value of 'Speed' to?", "SPEED",
                                           "", 1, 25)
            # Replace the current value with new one
            card_confirm[monster_name]["Speed"] = new_speed

        elif change == "Stealth":

            # Ask user for new value
            new_stealth = easygui.integerbox("What would you like to change "
                                             "the value of 'Stealth' to?",
                                             "STEALTH", "", 1, 25)
            # Replace the current value with new one
            card_confirm[monster_name]["Stealth"] = new_stealth

        elif change == "Cunning":

            # Ask user for new value
            new_cunning = easygui.integerbox("What would you like to change "
                                             "the value of 'Cunning' to?",
                                             "CUNNING", "", 1, 25)
            # Replace the current value with new one
            card_confirm[monster_name]["Cunning"] = new_cunning


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

# Card to change
new_card = {"STONELING":
                    {"Strength": 7, "Speed": 1, "Stealth": 25, "Cunning": 15}}

# Get the correct updated card
correct_card = change_card(new_card)

# Add the correct combo to the list of combos
exist_cards.update(correct_card)

print(exist_cards)
