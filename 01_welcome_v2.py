"""Version 2 of welcome and menu screen, trialling it a different way using
easygui"""

import easygui

# Print welcome statement
easygui.msgbox("Welcome to Monster Card Catalogue", "WELCOME")

# Ask user to choose an option
choice = easygui.buttonbox("What would you like to do?\n", "Options",
                           choices=["1) Add card","2) Search card",
                                    "3) Delete card","4) Output card",
                                    "5) Exit"])

# Testing the code to make sure it corresponds to the correct option
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

