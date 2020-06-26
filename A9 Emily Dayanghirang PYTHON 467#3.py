#--------------------------------------------------------------------------------------
# 467#3 Rainfall MODIFICATION
# Exercise 3 in Chapter 8 asked you to design a program that lets
# the user enter the total rainfall for each of 12 months into an array.
# (You will need to develop that program with the following modifications)
# Calculate and display the total rainfall for the year,
# the average monthly rainfall,
# and the months with the highest and lowest amounts.
# Enhance the program so it uses a 2 parallel arrays for months and rainfall,
# sorts the rainfall array in ascending order by amount of rainfall
# and displays the values (months and rainfall).
# Note: When sorting the rainfall, you have to perform the same sort on
# the months so the arrays stay parallel.
# This allows you display the correct months with the sorted rainfall amounts.
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
# Name:         Emily Dayanghirang
# Date:         05-04-2020
# Reference:    page # 467 problem # 03
# Title:        Rainfall MODIFICATION
# Inputs:       Amount of rainfall each month for a whole year
# Process:      (1) Sort the total rainfall for each 12 months in
#                   ascending order by amount of rainfall
#               (2) Calculate total rainfall, average monthly rainfall,
#                   highest and lowest amounts of rainfall
# Outputs:      (1) Display the total rainfall for each 12 months in
#                   ascending order by amount of rainfall
#               (2) Display calculations of total rainfall, average
#                   monthly rainfall, highest and lowest amounts
#                   of rainfall
#--------------------------------------------------------------------------------------

# Global constant SIZE (Number of months)
SIZE = 12

def main():

    # Declare months array
    months = ['January','February','March','April','May','June',
              'July','August','September','October','November',
              'December']
    
    # Declare amountOfRainfall array
    amountOfRainfall = [None] * SIZE

    # Initialize index variable to use for the first loop
    index = 0

    # Inform user to enter the total rainfall for each of 12 months
    print('Please enter the total rainfall for each of 12 months.')
    print('The program will display the amount of rainfall in')
    print('ascending order and their corresponding month.\n')
    
    # Loop for setting the value of each of the elements in the list
    while index < SIZE:
        
        # Prompt user to input names
        print('Month',index+1,'- Amount of rainfall: ',end='')
        amountOfRainfall[index] = int(input())

        # Prevents an infinite loop
        # Proceeds setting values to other elements
        index += 1

    # Sort the array in ascending order
    insertionSort(amountOfRainfall,months)

    # Reinitialize index variable to use for the loop to display contents
    index = 0

    # Inform user what will be displayed
    print('\nThe total rainfall for each of 12 months displayed')
    print('in ascending order by amount of rainfall:')

    # Loop for displaying the contents of the two arrays
    while index < SIZE:
        print(months[index],':',amountOfRainfall[index])
        index += 1

    # Call calculations module    
    calculations(amountOfRainfall)
    

# Modified the insertion sort from pg.458 of the Programming Logic And Design Book
def insertionSort(rainfallArray, monthsArray):

    # Initialize the index for the outer loop
    index = 1

    # The outer loop steps the index variable through
    # each subscript in the list, starting at 1. This
    # is because element 0 is considered already sorted.
    while index < SIZE:
        # The first element outside the sorted subset is
        # rainfallArray[index]. Assign the value of this element
        # to unsorted_value.
        unsorted_value = rainfallArray[index]
        
        # The first element outside the sorted subset is
        # monthsArray[index]. Assign the value of this element
        # to unsorted_month.        
        unsorted_month = monthsArray[index]

        # Start the scan variable at the subscript of the
        # first element outside the sorted subset.
        scan = index

        # Move the first element outside the sorted subset
        # into its proper position within the sorted subset.
        while scan > 0 and rainfallArray[scan - 1] > unsorted_value:
            rainfallArray[scan] = rainfallArray[scan - 1]
            monthsArray[scan] = monthsArray[scan - 1]
            scan = scan - 1

        # Insert the unsorted value and unsorted month in its proper position
        # within the sorted subset.
        rainfallArray[scan] = unsorted_value
        monthsArray[scan] = unsorted_month

        # Increment index
        index += 1

# Module for calculating and displaying
# the total rainfall, average monthly rainfall,
# highest and lowest amounts of rainfall
def calculations(rainfallArray):


    # Calculate total rainfall
    # As per the requirements, using sum function is not prohibited
    totalRainfall = sum(rainfallArray)

    # Calculate average monthly rainfall
    averageMonthlyRainfall = totalRainfall / SIZE

    # Calculate highest amount of rainfall
    highestAmountOfRainfall = rainfallArray[SIZE - 1]

    # Calculate lowest amount of rainfall
    lowestAmountOfRainfall = rainfallArray[0]

    # Display calculations
    print('\nThe total rainfall for the year is:', totalRainfall)
    print('The average monthly rainfall for the year is:', format(averageMonthlyRainfall,'.2f'))
    print('The highest amount of rainfall for the year is:', highestAmountOfRainfall)
    print('The lowest amount of rainfall for the year is:', lowestAmountOfRainfall)

main()
    
