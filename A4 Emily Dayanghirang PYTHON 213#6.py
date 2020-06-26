#---------------------------------------------------------------------------------------------
# Serendipity Booksellers has a book club that awards points to its customers
# based on the number of books purchased each month. The points are awarded as follows:

# ▪ If a customer purchases 0 books, he or she earns 0 points.

# ▪ If a customer purchases 1 book, he or she earns 5 points.

# ▪ If a customer purchases 2 books, he or she earns 15 points.

# ▪ If a customer purchases 3 books, he or she earns 30 points.

# ▪ If a customer purchases 4 or more books, he or she earns 60 points.

# Design a program that asks the user to enter
# the number of books that he or she has purchased this month

# and displays the number of books purchased
# and the number of points awarded.
#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
# Name:         Emily Dayanghirang
# Date:         02-28-2020
# Reference:    page # 213 problem # 06
# Title:        Book Club Points
# Inputs:       Number of books the user purchased this month
# Process:      Check conditions that determine the number of points awarded to the user
#               given the number of books purchased in the month
# Outputs:      Display number of books purchased and the points awarded
#---------------------------------------------------------------------------------------------

def main():

    # Initialize variables returned
    books=points=0

    introduction()
    numberOfBooks = getNumberOfBooks()
    numberOfPoints = getPoints(numberOfBooks)
    displayNumberOfBooks(numberOfBooks)
    displayNumberOfPoints(numberOfPoints)

    

# Explain the use of the program
def introduction():
    
    print('''\n    You will enter the number of books you purchased this month
    and the program will determine the number of points awarded to you.\n''')

    return

# Prompt user to enter number of books purchased this month
def getNumberOfBooks():

    books = int(input('Number of books purchased this month: '))

    return books


# Conditionally executed statements to get the points given the number of books
def getPoints(amountOfBooks):

    if amountOfBooks == 0:
        points = 0
    elif amountOfBooks == 1:
        points = 5
    elif amountOfBooks == 2:
        points = 15
    elif amountOfBooks == 3:
        points = 30
    elif amountOfBooks >=4:
        points = 60

    return points


# Display the number of books purchased by the user
def displayNumberOfBooks(books):

    print('\nThe number of books you purchased is ', books,'.', sep='')

    return
    
# Display the numebr of points awarded to the user
def displayNumberOfPoints(points):
    
    print('The number of points awarded to you is ', points,'.\n', sep='')

    return

# Call main function
main()
    
