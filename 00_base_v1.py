"""Monster Card Catalogue base component v1
Components added after they have been created and tested"""

import easygui


# Function to display welcome screen and menu
def welcome():
    # Print welcome statement
    easygui.msgbox("* * * Welcome to Monster Card Catalogue * * *", "WELCOME")
    # Ask user to choose an option
    option = easygui.buttonbox("What would you like to do?\n", "Options",
                               choices=["1) Add card","2) Search card",
                                        "3) Delete card","4) Output card",
                                        "5) Exit"])
    return option


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
choice = welcome()

# Will call on corresponding functions
if choice == "1) Add card":
    print("Add card")

elif choice == "2) Search card":
    print("Search card")

elif choice == "3) Delete card":
    print("Delete card")

elif choice == "4) Output card":
    print("Output card")

elif choice == "5) Exit":
    print("Exit")
