#----------------------------------------------------------------------------------------------------------------
# 413#7 Phone Number Lookup
# Design a program that has two parallel arrays:
# a String array named people that is initialized
# with the names of seven of your friends,
# and a String array named phoneNumbers
# that is initialized with your friends’ phone numbers.
# The program should allow the user to enter a person’s name
# (or part of a person’s name).
# It should then do a CASE INSENSITIVE
# search for that person in the people array.
# If the person is found, it should get that person’s phone number
# from the phoneNumbers array and display their name and phone number it.
# If the person is not found in the people array,
# the program should display a message indicating so.
#------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------
# Name:         Emily Dayanghirang
# Date:         04-20-2020
# Reference:    page # 413 problem # 07
# Title:        Phone Number Lookup
# Inputs:       Name of the person the user want to lookup for his or her phone number
# Process:      Does a Case-insensitive search in the people array for the name
#               the user entered
# Outputs:      (1) Name of the person the user entered that is found by the program
#               (2) The phone number of the person the user entered that is found by the program
#               (3) A display that informs the user when the person's name is not found
#------------------------------------------------------------------------------------------------------------------

def main():
    # Initialize String list with names
    people = ['Doniz','Matt','Mari','Rachelle','Alexis','Karen','Jessica']
    
    # Initialize String list with phone numbers
    phoneNumbers = ['1-800-3425627','1-800-3231232','1-800-2323882','1-800-2323232','1-800-1111111','1-800-2222222','1-800-3333333']

    # Prompt user
    nameToLookup = input('Enter the person\'s name you want to lookup for his/her phone number: ')

    # Declare Boolean variable found to False
    found = False

    # Declare Integer index variable to 0
    index = 0

    # Case-insensitive search for name in the people list
    while found == False and index < len(people):
        if people[index].lower() == nameToLookup.lower():
            # Set found variable to True if names match
            found = True
        else:
            # Proceed with iteration
            # Allows program to look up on other elements
            index += 1

    # Get the person's phone number and diplay their name and phone number
    if found:
        
        """ Use the same subscript, that is the value in the index variable,
            for accessing the related data in both the people list
            and phoneNumbers list"""

        # Set variables to display
        nameFound = people[index]
        phoneNumberFound = phoneNumbers[index]

        print(nameFound,':',phoneNumberFound)

    else:
        # Inform user when the person's name is not found
        print('The name you entered is not found.')

main()
            
