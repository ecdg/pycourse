#-----------------------------------------------------------------------------------
# Name: Emily Dayanghirang
# Date: 01-31-2020
# Reference: page # 99 problem # 04
# Title: Total Purchase
# Inputs: Price of each of the five items the user is purchasing
# Process: Calculates the subtotal, sales tax amount, and the total of the sale
# Outputs: The subtotal, sales tax amount, and the total of the sale
#-----------------------------------------------------------------------------------


def main():
    # Initializes the constant sales tax
    SALES_TAX = 0.06

    # Informs user the usage of the program
    print('''\n   You are to enter individually the price of each of the
                five items you are purchasing.    \n''')

    # Creates a list of the prices
    prices = []

    # Allows user to enter a price five times
    for i in range(5):
        price = float(input('Enter price: $'))
        prices.append(price)

    # Calculates the subtotal
    subtotal = sum(prices)
    
    # Calculates the sales tax amount
    salesTaxAmount = subtotal * SALES_TAX
    
    # Calculates the total
    total = subtotal + salesTaxAmount

    # Creates a line break
    print()

    # Displays subtotal with two decimal places
    print('SUBTOTAL: $', '{:.2f}'.format(subtotal), sep='')

    # Displays sales tax amount with two decimal places
    print('SALES TAX 6%: $', '{:.2f}'.format(salesTaxAmount), sep='')

    # Displays total of the sale with two decimal places
    print('TOTAL: $', '{:.2f}'.format(total), sep='')

    print()
    

# Executes main function
if __name__ == "__main__":
    main()

    
