"""Version 1 of welcome and menu screen without using easygui """


# Print welcome statement
print("Welcome to Monster Card Catalogue")

# Ask user to enter a number
choice = input("What would you like to do?\n"
               "1) Add card\n"
               "2) Search card\n"
               "3) Delete card\n"
               "4) Output card\n"
               "5) Exit\n"
               "Enter number here: ")

# Testing the code to make sure it corresponds to the correct option
if choice == "1":
    print("Add card")

elif choice == "2":
    print("Search card")

elif choice == "3":
    print("Delete card")

elif choice == "4":
    print("Output card")

elif choice == "5":
    print("Exit")
