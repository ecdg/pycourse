#----------------------------------------------------------------------------------------------------------
# 279#3 Budget Analysis
# Design a program that asks the user to enter the amount that he or she has budgeted for a month.
# A loop should then prompt the user to enter each of his or her expenses for the month,
# and keep a running total.
# Have the user enter a flag to stop the loop that is collecting expenses.
# The program should display the amount that the user is over or under budeget.
# You should also detect if the user is exactly on budget and handle accordingly.
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
# Name:         Emily Dayanghirang
# Date:         03/13/2020
# Reference:    page # 279 problem # 03
# Title:        Budget Analysis
# Inputs:       Budget for the month and each of the user's expenses for the month
# Process:      Conditionally execute statemens, using a repetition structure and decision structures;
#               Keeps a running total of the user's expenses every after prompting user to enter an expense;
#               Determine whether user is under, over, or exactly on budget        
# Outputs:      Total expenses, budget; and decision whether the user is under, over, or exactly on budget
#-----------------------------------------------------------------------------------------------------------

def main():
    # Initialize variables
    budget = 0.0
    expense = 0.0
    totalExpenses = 0.0
    
    # Prompt user to enter the amount of his or her budget for the month
    budget = float(input('Enter the amount that you have budgeted for the month: $'))
    # Create a line break
    print()
    ''' Prompt user to enter the amount of his or her first expense made in the month,
        or a negative value to end '''
    print ('Enter the amount of your first expense made in the month',
           '\n(or enter a negative value to end): $', end='')
    expense = float(input())
    print()

    ''' Prompt the user to enter another expense made in the month repeatedly
        until user decides to end '''
    while expense >= 0:
        # totalExpense is an accumulator to keep the running total of the user's expenses
        totalExpenses = totalExpenses + expense
        print ('Enter the amount of another expense made in the month',
               '\n(or enter a negative value to end): $', end='')
        expense = float(input())
        print()


        ''' Putting this section within the while loop prevents the program
            from printing any of the statements on here when the user
            decides to end the program in the second prompt
            that is outside the loop. '''
        
        ''' Statements execute only when user intends to end giving another
            input, by giving an input of a negative value. '''
        if not (expense >= 0):
            # Determine whether user is under, over, or exactly on budget
            if totalExpenses < budget:
                print ('Your total expenses of $', format(totalExpenses,'.2f'),
                       ' is under your budget of $', format(budget,'.2f'),'.',
                       sep='')
            elif totalExpenses > budget:
                print ('Your total expenses of $', format(totalExpenses,'.2f'),
                       ' is over your budget of $', format(budget,'.2f'),'.',
                       sep='')
            else:
                print ('Your total expenses of $', format(totalExpenses,'.2f'),
                       ' is exactly on your budget of $', format(budget,'.2f'),'.',
                       sep='')

main()
