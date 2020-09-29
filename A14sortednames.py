#-----------------------------------------------------------------------
# 467#2 Sorted Names
# Design a program that allows the user
# to enter 20 names into a String array.
# Make sure that you use a constant (SIZE = 20)
# and use the constant to setup your looping and sorting instead
# of hard coding 20 everywhere.
# Sort the array in ascending (alphabetical) order
# and display its contents.
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
# Name:         Emily Dayanghirang
# Date:         05-02-2020
# Reference:    page # 467 problem #02
# Title:        Sorted Names
# Inputs:       20 names in any order
# Process:      (1) The program will store the 20 names
#               given by the user into a String array.
#               (2) The program will sort the array in ascending order
#               (alphabetical order).
# Outputs:      The program will display the names given by the user
#               in alphabetical order.
#-----------------------------------------------------------------------

# Constant for the array size
SIZE = 20

def main():

    # Declare string array
    names = [None] * SIZE

    # Initialize index variable to use for the first loop
    index = 0

    # Prompt user to enter 20 names
    print('Please enter 20 names and the program will')
    print('sort the names in alphabetical order for you.\n')
    
    # Loop for setting the value of each of the elements in the list
    while index < SIZE:
        
        # Prompt user to input names
        names[index] = input('Name: ')

        # Prevents an infinite loop
        # Proceeds setting values to other elements
        index += 1

    # Sort the array in alphabetical order
    insertionSort(names)

    # Reinitialize index variable to use for the loop to display contents
    index = 0

    # Inform user that the names will now be displayed
    print('\nHere are the names you entered displayed in alphabetical order:')

    # Loop for displaying the contents of the array
    while index < SIZE:
        print(names[index])
        index += 1

# Insertion sort from pg.458 of the Programming Logic And Design Book
def insertionSort(array):

    # Initialize the index for the outer loop
    index = 1

    # The outer loop steps the index variable through
    # each subscript in the list, starting at 1. This
    # is because element 0 is considered already sorted.
    while index < SIZE:
        # The first element outside the sorted subset is
        # array[index]. Assign the value of this element
        # to unsorted_value.
        unsorted_value = array[index]

        # Start the scan variable at the subscript of the
        # first element outside the sorted subset.
        scan = index

        # Move the first element outside the sorted subset
        # into its proper position within the sorted subset.
        while scan > 0 and array[scan - 1] > unsorted_value:
            array[scan] = array[scan - 1]
            scan = scan - 1

        # Insert the unsorted value in its proper position
        # within the sorted subset.
        array[scan] = unsorted_value

        # Increment index
        index += 1
        
main()
