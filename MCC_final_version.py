"""FINAL OUTCOME of Monster Card Catalogue"""

import easygui


# Function to display welcome screen and menu
def welcome():
    # Ask user to choose an option
    task = easygui.buttonbox("What would you like to do?\n", "Options",
                             choices=["1) Add card", "2) Search card",
                                      "3) Delete card", "4) Output catalogue",
                                      "5) Exit"])
    while task != "5) Exit":

        # Will call on corresponding functions
        if task == "1) Add card":
            add_card(exist_cards)
            welcome()

        elif task == "2) Search card":
            search_card(exist_cards)
            welcome()

        elif task == "3) Delete card":
            delete_card(exist_cards)
            welcome()

        elif task == "4) Output catalogue":
            output(exist_cards)
            welcome()

    # Print goodbye message
    easygui.msgbox("Thank you for using the catalogue", "GOODBYE")
    exit()


# Function to make sure input is entered and not left blank
def blank_checker(question, title, box):
    error_message = "You must fill out every field"

    if box == "enter":
        # Asks user for input
        answer = easygui.enterbox(question, title)

        while True:  # Loops until valid input is entered
            if answer == "":  # Checks if it is blank
                easygui.msgbox(error_message, "ERROR")  # Show error message
                answer = easygui.enterbox(question, title)

            if not answer:
                welcome()

            else:
                return answer

    elif box == "integer":
        # Asks user for input
        answer = easygui.integerbox(question, title, lowerbound=1,
                                    upperbound=25)

        while True:  # Loops until valid input is entered
            if not answer:
                welcome()
            else:
                return answer


# Function to allow user to add a new card
def add_card(cards):

    new_card = {}

    # Get the values for each category
    monster_name = blank_checker("Enter the monster's name", "NAME",
                                 "enter").upper()
    # Check if the name has already been used
    while monster_name in exist_cards:
        # Show error message
        easygui.msgbox(f"Sorry, {monster_name} is already the name of a "
                       f"monster card\n You must enter a different name",
                       "ERROR")
        # Ask for name again
        monster_name = blank_checker("Enter the monster's name", "NAME",
                                     "enter").upper()

    strength = blank_checker("Enter the value for 'Strength'\n Between 1 and "
                             "25", "STRENGTH", "integer")
    speed = blank_checker("Enter the value for 'Speed'\n Between 1 and 25",
                          "SPEED", "integer")
    stealth = blank_checker("Enter the value for 'Stealth'\n Between 1 and "
                            "25", "STEALTH", "integer")
    cunning = blank_checker("Enter the value for 'Cunning'\n Between 1 and "
                            "25", "CUNNING", "integer")

    # Add the user's card to a new dictionary

    # Adds key with monster name and empty dictionary
    new_card[monster_name] = {}
    new_card[monster_name]["Strength"] = strength  # Adds strength
    new_card[monster_name]["Speed"] = speed  # Adds speed
    new_card[monster_name]["Stealth"] = stealth  # Adds stealth
    new_card[monster_name]["Cunning"] = cunning  # Adds cunning

    # Get the correct updated card
    correct_card = change_card(new_card)

    # Add the correct card to the existing catalogue
    cards.update(correct_card)


# Function to allow user to edit the card
def change_card(card_confirm):
    # Keep looping until the card is correct
    while True:
        monster_name = ""

        # Print the card and check with user that it is correct
        card = ""
        for monster_name, card_info in card_confirm.items():

            for category in card_info:
                card += f"{category}: {card_info[category]}\n"

        confirm = easygui.buttonbox(f"Is the following card correct?\n\n"
                                    f"{monster_name}\n\n"
                                    f"{card}", "CONFIRM",
                                    choices=["Yes", "No"])

        # When user is happy with the card

        if confirm == "Yes":
            easygui.msgbox(f"You have successfully confirmed the card "
                           f"{monster_name}", "CARD CONFIRMED")
            return card_confirm

        # Ask the user what they would like to change
        change = easygui.buttonbox("What would you like to change?",
                                   "CATEGORIES",
                                   choices=["Monster name", "Strength",
                                            "Speed", "Stealth", "Cunning"])

        if change == "Monster name":

            # Ask user for new monster name
            monster_name_change = blank_checker("What would you like to "
                                                "change it to?", "NAME",
                                                "enter").upper()

            # If the name has already been used
            while monster_name_change in exist_cards:
                # Error message
                easygui.msgbox(f"{monster_name_change} is already the "
                               f"name of a monster card in the deck\n You "
                               f"must choose a different name",
                               "ERROR")

                # Ask user for new monster name
                monster_name_change = blank_checker("What would you like to "
                                                    "change it to?\n "
                                                    "Between 1 and 25",
                                                    "NAME", "enter").upper()

            # Replace the monster name with new name
            card_confirm[monster_name_change] = card_confirm.pop(monster_name)

        elif change == "Strength":

            # Ask user for new value
            new_strength = blank_checker(
                "What would you like to change the value "
                "of 'Strength' to?\n Between 1 and 25", "STRENGTH",
                "integer")
            # Replace the current value with new one
            card_confirm[monster_name]["Strength"] = new_strength

        elif change == "Speed":

            # Ask user for new value
            new_speed = blank_checker(
                "What would you like to change the value "
                "of 'Speed' to?\n Between 1 and 25", "SPEED", "integer")
            # Replace the current value with new one
            card_confirm[monster_name]["Speed"] = new_speed

        elif change == "Stealth":

            # Ask user for new value
            new_stealth = blank_checker(
                "What would you like to change the value "
                "of 'Stealth' to?\n Between 1 and 25", "STEALTH", "integer")
            # Replace the current value with new one
            card_confirm[monster_name]["Stealth"] = new_stealth

        elif change == "Cunning":

            # Ask user for new value
            new_cunning = blank_checker("What would you like to change the "
                                        "value of 'Cunning' to?\n Between 1 "
                                        "and 25", "CUNNING",
                                        "integer")
            # Replace the current value with new one
            card_confirm[monster_name]["Cunning"] = new_cunning


# Function to allow user to search for a monster card
def search_card(cards):

    while True:
        # Ask user to enter monster name they want to search
        search_name = blank_checker("Enter name of monster card", "SEARCH",
                                    "enter").upper()

        while search_name not in cards:
            easygui.msgbox(f"Sorry, {search_name} is not in the catalogue",
                           "ERROR")
            # Ask user to enter monster name they want to search
            search_name = blank_checker("Enter name of monster card",
                                        "SEARCH", "enter").upper()

        # Add the searched card to a separate dictionary
        searched_card = {search_name: cards[search_name]}

        # Confirm the dictionary with user
        correct_card = change_card(searched_card)

        # Delete the original card
        del[cards[search_name]]

        # Add the changed correct card
        cards.update(correct_card)

        break


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
    if not card_del:
        welcome()

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


# Function to output the full catalogue
def output(cards):

    catalogue = ""

    # Loop to print full catalogue
    for monster_name, monster_info in cards.items():

        # Print the combo name
        catalogue += f"\n* * {monster_name} * * \n"

        # Print the combo items and price
        for key, value in monster_info.items():
            catalogue += f"{key}: {value} \n"
        catalogue += "--------------------"

    # Output the full menu
    print(f"/ / / Below is the full catalogue/ / /\n"
          f"{catalogue}\n\n")

    welcome()


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

# Print welcome statement
easygui.msgbox("* * * Welcome to Monster Card Catalogue * * *", "WELCOME")
welcome()
