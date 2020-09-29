#-----------------------------------------------------------------------------------
# Name: Emily Dayanghirang
# Date: 02-01-2020
# Reference: page # 99 problem # 08
# Title: Tip, Tax, and Total
# Inputs: Cost of a meal from a restaurant
# Process: Calculates the sales tax amount, tip amount, and the total of a meal
# Outputs: The subtotal, sales tax amount, tip amount, and the total of a meal
#-----------------------------------------------------------------------------------


def main():
    # Initializes the constant sales tax
    SALES_TAX = 0.07

    # Initializes the constant tip rate
    TIP_RATE = 0.15

    # Informs user what the program does
    print('''\n This program will calculate the total amount of the meal
            you are purchasing from the restaurant.\n''')
    
    # Creates a line break
    print()

    # Allows user to enter the cost of a meal
    subtotal = float(input("Enter cost of the meal: $"))

    # Calculates the sales tax amount
    salesTaxAmount = subtotal * SALES_TAX

    # Calculates the tip amount
    tipAmount = subtotal * TIP_RATE

    # Calculates the total
    total = subtotal + salesTaxAmount + tipAmount

    print()

    # Displays subtotal with two decimal places
    print('SUBTOTAL: $', '{:.2f}'.format(subtotal), sep='')

    # Displays sales tax amount with two decimal places
    print('SALES TAX 7%: $', '{:.2f}'.format(salesTaxAmount), sep='')

    # Displays tip amount with two decimal places
    print('TIP 15%: $', '{:.2f}'.format(tipAmount), sep='')    

    # Displays total of the sale with two decimal places
    print('TOTAL: $', '{:.2f}'.format(total), sep='')

    print()
    

# Executes main function
if __name__ == "__main__":
    main()

    
