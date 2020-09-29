#-----------------------------------------------------------------------------
# Name:         Emily Dayanghirang
# Date:         02/15/2020
# Reference:    page # 121 problem # 01
# Title:        Kilometer Converter
# Inputs:       Distance in kilometers
# Process:      Converts kilometers to miles
# Outputs:      Distance in kilometers and distance in miles
#-----------------------------------------------------------------------------

def main():

    # Initializes kmDistance and miDistance
    kmDistance = 0.0
    miDistance = 0.0

    # Explains what the program does
    print('\nThis program will convert distance in kilometers to miles.\n')

    # Stores user input from getKmDistance() to kmDistance variable
    kmDistance = getKmDistance()

    # Stores converted value result to miDistance variable
    miDistance = convertToMiles(kmDistance)

    # Prints new line
    print()
    # Displays distance in kilometers
    print('The distance in kilometers is', '{:.2f}'.format(kmDistance),'km.')
    # Displays distance in miles
    print('The distance in miles is', '{:.2f}'.format(miDistance),'mi.')
    print()

def getKmDistance():

    # Initializes km
    km = 0.0

    # Allows int or float input only
    while True:
        try:
            # Takes user input
            km = float(input('Enter the distance in kilometers: '))
            break
        
        except ValueError:
            print('Invalid input.\n')

    return km

def convertToMiles(km):

    # Initializes miles
    miles = 0.0

    # Computes for miles
    miles = km * 0.6214

    return miles

# Calls main function
main()
