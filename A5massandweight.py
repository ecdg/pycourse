#---------------------------------------------------------------------------------------
#Scientists measure an object’s mass in kilograms and its weight in Newtons.

#If you know the amount of mass of an object, you can calculate its weight,
#in Newtons, with the following formula:
    
#Weight=Mass × 9.8

#Design a program that asks the user to enter
#an object’s mass, and then calculates its weight.

#➔Display the mass and the weight in Newtons.

#If the object weighs more than 1,000 Newtons,
#display a message indicating that it
#weighs > 1,000 Newtons and is too heavy.

#If the object weighs less than 10 Newtons,
#display a message indicating that it
#weighs < 10 Newtons and is too light.
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
#Name:       Emily Dayanghirang
#Date:       02-26-2020
#Reference:  page # 213 problem # 03
#Title:      Mass and weight (with modification)
#Inputs:     Mass
#Process:    Calculate Weight in Newtons,
#            Check conditions that describe the object's weight
#Outputs:    Mass and Weight. In addition, the program displays a message indicating
#            an object to be too heavy, too light, or an object's weight is within range.
#-----------------------------------------------------------------------------------------



def main():

    # Initialize variables returned
    mass=weight=0

    introduction()
    objectMass = getMass()
    objectWeight = calculateWeight(objectMass)
    displayMassAndWeight(objectMass, objectWeight)
    messageResult(objectWeight)

# Explain what the program does
def introduction():

    print('''\n    You will enter the mass of an object and this program will calculate
    the weight of the object in Newtons. In addition, this program will
    alert you whether the object is too heavy, too light, or within range.\n''')

    return

# Prompt user to enter an object's mass
def getMass():

    mass = float(input('Enter the object\'s mass: '))

    return mass

# Calculate for the weight
def calculateWeight(mass):


    weight = mass * 9.8

    return weight

# Display mass and weight
def displayMassAndWeight(mass, weight):

    print('\nThe mass of the object is', format(mass,'.2f'),'kg.')
    print('The weight of the object is ', format(weight,'.2f'),'N.')

    return

# Conditonally executed statements that describe the object's weight
def messageResult(weight):

    # Display a message indicating the object to be too heavy
    if weight > 1000:
        print('\nThe object weighs > 1,000 Newtons. The object is too heavy.\n')
    # Display a message indicating the object to be too light
    elif weight < 10:
        print('\nThe object weighs < 10 Newtons. The object is too light.\n')
    # Display a message indicating the object's weight is within range
    else:
        print('\nThe object\'s weight is within range.\n')

    return

# Call main function
main()

        


