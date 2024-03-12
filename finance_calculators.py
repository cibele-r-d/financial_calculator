import math
from sys import exit

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan\n") # Create a new line before the next input
 
 

while True:
    # Function strip() is added in case user accidentally add empty spaces
    invest_or_bond = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").strip().lower()
    
    if invest_or_bond not in ["investment", "bond"]:
        print("We only deal with investments or bonds, please try again") # In this case the program reprompt investment_bond input
        continue

    elif invest_or_bond == "investment":

        while True:
            try:
                deposit = input("Enter the amount you would like to invest: £")
                if "," in deposit:
                    deposit = deposit.replace(",", "")

                deposit = float(deposit) #CORRECTION: deposit is now converted to float

                rate = input("Enter the interest rate expected for your investment: ")
                rate = int(rate)/100 

                time = int(input("Enter the number of years you intend to invest: "))


                while True:
                    interest = input("Enter what investment would like, please type 'simple' or 'compound': ").strip().lower()
                    if interest not in ["simple", "compound"]:
                        print("We only deal with simple or compound investments, please try again") # In this case the program reprompt interest input
                        continue
                        
                    elif interest == "simple":
                        amount = int(deposit) *(1 + (rate)*time)
                        exit(f"At the end of {time} years your total amount will be £{float(amount):,.2f}") #value is a float with 2 decimal digits and thousands is separated by a comma
                        

                    elif interest == "compound":
                        amount = deposit * math.pow((1+(rate)), time)
                        exit(f"At the end of {time} years your total amount will be £{float(amount):,.2f}")
                        

            except ValueError:
                print("Please enter a number for the deposit, interest rate, and years.")
            except TypeError:
                print("Invalid input. Please make sure to enter numbers only.")

    elif invest_or_bond == "bond":
        
        while True:
            try:    
                house_value = input("Enter the current price of the house: £")
                if "," in house_value:
                    house_value = house_value.replace(",", "")

                house_value = float(house_value)

                rate_house = input("Enter the interest rate for your bound: ")
                rate_house = (int(rate_house)/100)/12       #CORRECTION rate is firstly divided by 100 and then by 12

                installments = int(input("Enter the number of monthly installments: ")) #CORRECTION spelling corrected

                repayments = (rate_house * house_value)/(1 - (1 + rate_house)**(-installments))        #CORRECTION spelling corrected
                exit(f"Total of {installments} installments of £{float(repayments):,.2f} ")
                


            except ValueError:
                print("Please enter house price, interest rate, and number of monthly installments.")
            except TypeError:
                print("Invalid input. Please make sure to enter numbers only.")            



