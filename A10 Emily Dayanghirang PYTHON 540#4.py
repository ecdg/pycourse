# 540 #4 Avg of Numbers
# Create a file (using notepad)
# containing a series of 15 integers
# named numbers.dat in the same folder as your program.
# Develop a program that
# reads the numbers
# and calculates
# the average of all the numbers stored in the file.
# Display the numbers and the average.
# (You don’t need to submit the numbers.dat file
# with your assignment. I have one to use to test/grade with.)
#--------------------------------------------------------------------------------------------
# Name:         Emily Dayanghirang
# Date:         05-11-2020
# Reference:    page # 540 problem # 04    
# Title:        Avg of Numbers
# Inputs:       None
# Process:      Reads numbers from a file and calculates the average of all the numbers
#               stored in the file
# Outputs:      Displays the numbers and the average of the numbers
#--------------------------------------------------------------------------------------------

def main():

    # Open the numbers file for reading
    numbersFile = open('numbers.dat', 'r')

    # Counter for the numbers count in the file
    numbersCount = 0

    # Accumulator for the total of the numbers in the file
    total = 0

    # Used to store the number per line in the file
    number = 0

    # Used to store average
    average = 0

    # Display the numbers in the file using a for loop
    print('Here are the numbers in the file:')
    # Read all the lines from the file
    for line in numbersFile:
        # Add 1 to numbersCount every after reading a line
        numbersCount += 1
        
        # Convert line to an integer.
        number = int(line)
    
        # Add number to the total accumulator
        total += number
        
        # Display the number
        print(number)

    # Close the file.
    numbersFile.close()

    # Calculate the average
    average = total/numbersCount

    print()
    # Display Average
    print('The average of the numbers in the file is:')
    print(format(average,'.2f'))
    
main()
