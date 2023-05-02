"""Welcome/ Menu Function
based on 01_welcome_v3, later after I have developed the other functions I
will replace the print statements with function calls"""

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
