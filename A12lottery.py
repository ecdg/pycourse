#--------------------------------------------------------------------------------------------
# 413#2 Lottery Number Generator
# Design a program that generates a 7-digit lottery number.
# The program should have an Integer array with 7 elements.
# Write a loop that steps through the array,
# randomly generating a number in the range of 0 through 9 for each element.
# (Use the random function that was discussed in Chapter 6.)
# Then write another loop that displays the contents of the array.
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
# Name:         Emily Dayanghirang
# Date:         04-20-2020
# Reference:    page # 413 problem # 02
# Title:        Lottery Number Generator
# Inputs:       None
# Process:      Randomly generates a number for each of the elements in the list/array,
#               in the range of 0 through 9
# Outputs:      The contents of the list/array
#--------------------------------------------------------------------------------------------
import random

def main():

    # Introduction for the program
    print('This program generates a 7-digit lottery number')

    # lotteryNumber Integer list to hold all 7 digits
    # Set all 7 elements with the value 0
    lotteryNumber = [0,0,0,0,0,0,0]

    # Initialize NumberOfDigits variable to use for the loops
    numberOfDigits = len(lotteryNumber)

    # Initialize index variable to use for the first loop
    index = 0

    # Loop for setting the value of each of the elements in the list
    while index < numberOfDigits:

        # Randomly generate the value to be set in the range of 0 through 9
        lotteryNumber[index] = random.randint(0,9)

        # Prevents an infinite loop
        # Proceeds setting values to other elements
        index += 1

    # Reinitialize index variable to use for the second loop
    index = 0

    # Loop for displaying the contents of the array
    while index < numberOfDigits:
        print(lotteryNumber[index])
        index += 1

main()
