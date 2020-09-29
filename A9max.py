#---------------------------------------------------------------------------
# 328#4 Max of 2 values
# Design and code a function named max
# that accepts two integer values as arguments
# and returns the value that is the greater of the two.
# For example, if 7 and 12 are passed as arguments to the function,
# the function should return 12.
# The function should detect when the two integers entered are equal.
# In that case, it should tell the user
# and prompt for 2 more numbers.
# Use the function in a program that prompts the user
# to enter two integer values.
# The program should display the value
# that is the greater of the two.
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
# Name:         Emily Dayanghirang
# Date:         03-28-2020
# Reference:    page # 328 problem # 04
# Title:        Max of 2 values
# Inputs:       Two integer values
# Process:      Determines the greater value between two values using
#               a max function
# Outputs:      Max value
#---------------------------------------------------------------------------

def main():
    # Initialize variables
    val1=val2=num1=num2=0
    
    # Display what the program does
    print('''    Provide two integer values and the program will return
    the value that is the greater of the two.\n''')

    # Prompt user for two values
    val1 = int(input('Enter the first value: '))
    val2 = int(input('Enter the second value: '))

    # Display line break
    print()

    # Determine greater value between two values
    # Using max function
    maxval = max(val1,val2)

    # Display the greater value between two values
    print('The greater value between the two values is ',maxval,'.',sep='')

def max(num1,num2):
    # Detect when the two integers entered are equal
    while(num1 == num2):
        print('The two integers are equal. Please provide two values again.\n')
        # Reprompt user
        num1 = int(input('Enter the first value: '))
        num2 = int(input('Enter the second value: '))
        print()

    # Determine the greater value and return that value
    if num1 > num2:
        return num1
    else:
        return num2
    
main()
