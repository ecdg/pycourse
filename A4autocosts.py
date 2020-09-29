#-------------------------------------------------------------------------------------------------------------------
# Name:         Emily Dayanghirang
# Date:         02/15/2020
# Reference:    page # 121 problem # 04
# Title:        Auto Costs
# Inputs:       Loan payment, insurance payment, gas payment, oil payment, tires expenses, and maintenance expenses
# Process:      Computes the total monthly cost and total annual cost of user's operation of his or her automobile
# Outputs:      Total monthly cost and total annual cost of user's operation of his or her automobile
#-------------------------------------------------------------------------------------------------------------------

def main():
    
    # Initialize variables
    loanPay=insurancePay=gasPay=oilPay=tiresExp=maintenanceExp=monthlyExp=annualExp= 0.0

    # Call introduction function
    introduction()

    # Store results to variables from function calls
    loanPay = loanPayment()
    insurancePay = insurancePayment()
    gasPay = gasPayment()
    oilPay = oilPayment()
    tiresExp = tiresCost()
    maintenanceExp = maintenanceCost()

    monthlyExp = monthlyCost(loanPay,insurancePay,gasPay,oilPay,tiresExp,maintenanceExp)
    annualExp = annualCost(monthlyExp)

    # Call results function
    results(monthlyExp,annualExp)

def introduction():
    
    # Explain the process of the program
    print('''\n    This program will compute your total monthly cost
    and total annual cost from operating your automobile.\n''')
    return

def loanPayment():

    # Initialize loan variable
    loan = 0.0
    # Take user input
    loan = float(input('Enter your monthly automobile loan payment: $'))
    return loan

def insurancePayment():

    # Initialize insurance variable
    insurance = 0.0
    # Take user input
    insurance = float(input('Enter your monthly automobile insurance payment: $'))
    return insurance

def gasPayment():

    # Initialize gas variable
    gas = 0.0
    # Take user input
    gas = float(input('Enter your monthly automobile gas payment: $'))
    return gas

def oilPayment():
    
    # Initialize oil variable
    oil = 0.0
    # Take user input
    oil = float(input('Enter your monthly automobile oil payment: $'))
    return oil

def tiresCost():
    
    # Initialize tires variable
    tires = 0.0
    # Take user input
    tires = float(input('Enter your monthly automobile tires expenses: $'))
    return tires

def maintenanceCost():

    # Initialize maintenance variable
    maintenance = 0.0
    # Take user input
    maintenance = float(input('Enter your monthly automobile maintenance expenses: $'))
    return maintenance

def monthlyCost(loan,insurance,gas,oil,tires,maintenance):

    # Initialize monthly variable
    monthly = 0.0
    # Compute for the monthly cost
    monthly = loan + insurance + gas + oil + tires + maintenance
    return monthly

def annualCost(monthly):

    # Initialize annual variable
    annual = 0.0
    # Compute for the annual cost
    annual = monthly * 12
    return annual

def results(monthly,annual):

    # Print new line
    print()
    # Print out results
    print('Your total monthly cost of operating your automobile is: $', '{:.2f}'.format(monthly), sep='')
    print('Your total annual cost of operating your automobile is: $', '{:.2f}'.format(annual), sep='')
    print()
    return

# Call main function
main()
    

