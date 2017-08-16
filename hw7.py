from sortedcontainers import SortedDict

"""
This script was modified for Homework 7.
The script works with a dictionary to find and modify values.
"""

def print_menu():
    print('1. Print Users')
    print('2. Add a User')
    print('3. Remove a User')
    print('4. Lookup a Phone Number')
    print('5. Quit')
    print()


# Create dictionary with key = Names, value = user_name
usernames = SortedDict()
usernames['Summer'] = 'summerela'
usernames['William'] = 'GoofyFish'
usernames['Steven'] = 'LoLCat'
usernames['Zara'] = 'zanyZara'
usernames['Renato'] = 'songDude'

# setup counter to store menu choice
menu_choice = 0

# display your menu
print_menu()

# as long as the menu choice isn't "quit" get user options
while menu_choice != 5:
    # get menu choice from user
    menu_choice = int(input("Type in a number (1-5): "))

    # View the current users contained in the dictionary
    if menu_choice == 1:
        print("Current Users:")
        for x, y in usernames.items():
            print("Name: {} \tUser Name: {} \n".format(x, y))

    # Add a user to the dictionary
    elif menu_choice == 2:
        print("Add User")
        name = input("Name: ")
        username = input("User Name: ")
        usernames[name] = username
        if not name or not username:   # Handles exception for empty name or username
            print("Please enter a valid name.")
            name = input("Name: ")
            username = input("User Name: ")
            usernames[name] = username

    # Remove a user from the dictionary
    elif menu_choice == 3:
        print("Remove User")
        name = input("Name: ")
        if name in usernames:
            usernames.pop(name)  # delete that entry
        else:
            print("Please try again with a valid name.")  # Handles exceptions

    # Lookup user
    elif menu_choice == 4:
        print("Lookup User")
        name = input("Name: ")
        if name in usernames:
            print(f'{name} was found in the dictionary')  # print the username
        else:
            print(f'{name} was not found in the dictionary') # print username not found

    # If the user enters a value other than 1-5, display the main menu again.
    elif menu_choice != 5:
        print("Please enter a valid option.")  # Prompts the user to enter a valid option to try again
        print_menu()
