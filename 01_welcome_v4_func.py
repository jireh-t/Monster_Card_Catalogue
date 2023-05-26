"""Welcome/ Menu Function
based on 01_welcome_v3, later after I have developed the other functions I
will replace the print statements with function calls"""

import easygui


# Function to display welcome screen and menu
def welcome():
    # Ask user to choose an option
    task = easygui.buttonbox("What would you like to do?\n", "OPTIONS",
                               choices=["1) Add card", "2) Search card",
                                        "3) Delete card", "4) Output "
                                                          "catalogue",
                                        "5) Exit"])
    while task != "5) Exit":

        # Will call on corresponding functions
        if task == "1) Add card":
            print("Add Card")
            welcome()

        elif task == "2) Search card":
            print("Search Card")
            welcome()

        elif task == "3) Delete card":
            print("Delete Card")
            welcome()

        elif task == "4) Output catalogue":
            print("Output catalogue")
            welcome()

    # Print goodbye message
    easygui.msgbox("Thank you for using the catalogue", "GOODBYE")
    exit()


# Main Routine
welcome()

