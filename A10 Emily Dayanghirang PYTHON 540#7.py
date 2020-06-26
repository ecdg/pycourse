# 540 #7 Best Golf Score
# (You will need to develop that flowchart and python program)
# Read from keyboard golfer names and scores
# and write them to golf.dat
# Read names and scores from golf.dat and display them

# Find the lowest score
# and display the player’s name and the score.
#---------------------------------------------------------------------------------------------
# Name:         Emily Dayanghirang
# Date:         05-11-2020
# Reference:    page # 540 problem # 07
# Title:        Best Golf Score
# Inputs:       Golfer Names and Scores
# Process:      (1) Write to golf.dat input from keyboard
#               (2) Read names and scores from golf.dat
#               (3) Find the lowest score
#
# Outputs:      (1) Display names and scores from golf.dat
#               (2) Display the lowest score and the player/s who owns that score
#--------------------------------------------------------------------------------------------
def main():

    # Open the golf.dat file to write data on it
    golfFile = open('golf.dat', 'w')

    # Declare players list to store the players' names
    players = []

    # Declare scores list to store all the scores
    scores = []

    # Declare scoreEntry list to store both the players' names and scores
    scoreEntry = []

    # Declare scoresTogether to be used to make a 2D list later
    scoresTogether = []

    # To be used for prime reading before the loop starts
    continueGettingNamesAndScores = 'y'

    while continueGettingNamesAndScores.lower() == 'y':

        # User inputs name
        playerName = input('Player name: ')

        # User inputs scores
        playerScore = int(input('Player score: '))

        # Append player name entry to players list
        players.append(playerName)

        # Append scores entry to scores list
        scores.append(playerScore)

        # Set the player name entry and score entry to the scoreEntry list
        scoreEntry = [playerName, playerScore]

        # Append to the scoresTogether 2D list the scoreEntry contents
        scoresTogether.append(scoreEntry)
        
        print()
        # Asks user if he/she wants to add more golfer names and scores
        continueGettingNamesAndScores = input('Continue adding golfer names and scores?(y for yes/n for no): ')
        print()


    # Display the data written out on the file
    print('Data written out is: ') 
    for scoreEntry in scoresTogether:
        
        # Create string holding the player's name and score and write it to the file.
        fileLine = scoreEntry [0] + " : " + str (scoreEntry [1]) + "\n"
        golfFile.write (fileLine)
        print(fileLine)

    # Close the file
    golfFile.close()


    # Open golf.dat file for reading
    golfFile = open('golf.dat', 'r')

    # Display the data read in on the file
    print('Data read in is: ')
    for line in golfFile:
    # Split the line with the delimiter (:)
    # to form 2 strings in the splitLine list
        splitLine = line.split (": ")
        # Create the score entry list/array with the first split string (name) and the
        # second string converted to an integer (score).
        scoreEntry = [splitLine [0], int(splitLine [1])]
        print(scoreEntry)

    # Close the file
    golfFile.close()

    print()

    # Take the size of the scores list to be used for sorting function
    # And for a loop that will display the player/s with the
    # lowest score
    size = len(scores)

    # Call the insertion sort to sort both the scores list and players list
    # based on the ascending order of the scores list
    insertionSort(scores, players, size)

    # Initialize index to 0 to be used for the loop
    index = 0

    # Display the player/s that own/s the lowest score
    # Also display the lowest score
    print('Lowest score belong/s to:')
    while index < size:
        if scores[index] == scores[0]:
            print('Player:', players[index],'Score:', scores[index])
        index += 1

def insertionSort(scores, players, size):

    # Initialize the index for the outer loop
    index = 1

    # The outer loop steps the index variable through
    # each subscript in the list, starting at 1. This
    # is because element 0 is considered already sorted.
    while index < size:
        # The first element outside the sorted subset is
        # scores[index]. Assign the value of this element
        # to unsorted_value.
        unsorted_value = scores[index]
        
        # The first element outside the sorted subset is
        # players[index]. Assign the value of this element
        # to unsorted_player.        
        unsorted_player = players[index]

        # Start the scan variable at the subscript of the
        # first element outside the sorted subset.
        scan = index

        # Move the first element outside the sorted subset
        # into its proper position within the sorted subset.
        while scan > 0 and scores[scan - 1] > unsorted_value:
            scores[scan] = scores[scan - 1]
            players[scan] = players[scan - 1]
            scan = scan - 1

        # Insert the unsorted value and unsorted player in its proper position
        # within the sorted subset.
        scores[scan] = unsorted_value
        players[scan] = unsorted_player

        # Increment index
        index += 1
        
main()
