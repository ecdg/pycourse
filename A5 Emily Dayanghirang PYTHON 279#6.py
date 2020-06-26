#----------------------------------------------------------------------------------------------------------
# 279#6 Distance Traveled
# The distance a vehicle travels can be calculated as follows:
# Distance = Speed × Time
# Design a program that asks the user for the speed of a vehicle
# (in miles per hour)
# and how many hours it has traveled.
# It should then use a loop to display the distance the vehicle
# has traveled for each hour of that time period.
# Here is an example of the output:
# What is the speed of the vehicle in mph? 70 [Enter]
# How many hours has it traveled? 3 [Enter]
# Hour      Distance Traveled
# ----------------------------
# 1         70
# 2         140
# 3         210
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
# Name:         Emily Dayanghirang
# Date:         03/13/2020
# Reference:    page # 279 problem # 06
# Title:        Distance Traveled
# Inputs:       Speed of a vehicle (in mph) and hours traveled
# Process:      Calculates for the distance traveled
# Outputs:      Hour and distance traveled every hour
#-----------------------------------------------------------------------------------------------------------

def main():

    # Initialize variables
    speed = 0.0
    hoursTraveled = 0
    distanceTraveled = 0.0

    # Prompt user to input speed
    speed = float(input('What is the speed of the vehicle in mph?: '))
    # Create a line break
    print()
    # Prompt user to input hours traveled
    hoursTraveled = int(input('How many hours has the vehicle traveled?: '))
    print()

    # Initialize the variable to hold the maximum value for the loop
    ''' This way, we perform the calculation once,
        instead of performing the addition to the stop value in the loop
        every time the loop tests. '''
    maxValue = hoursTraveled + 1

    # Display heading
    print('Hour\tDistance Traveled')
    print('-------------------------')
    
    # Count-controlled loop that displays the distance traveled every hour
    for hour in range(1, maxValue):
        # Calculate for the distance traveled
        distanceTraveled = speed * hour
        print(hour, '\t', format(distanceTraveled,'.2f'))

main()
