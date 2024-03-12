import math
from sys import exit

def start_again():
    choice = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
    if choice != "yes":
        exit("Thank you for using our calculator. Goodbye!")
        
        


print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan\n") # Create a new line before the next input
 
 

while True:
    print("Welcome to the financial calculator!")
    print("Please select one of the following options:")
    print("1. Investment - Calculate the amount of interest you'll earn on your investment.")
    print("2. Bond - Calculate the amount you'll have to pay on a home loan.")
    print("Type 'exit' to quit the program.\n")

    option = input("Enter the option number to proceed: ")

    if option == "1":
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
                        print(f"At the end of {time} years your total amount will be £{float(amount):,.2f}") #value is a float with 2 decimal digits and thousands is separated by a comma
                        break 

                    elif interest == "compound":
                        amount = deposit * math.pow((1+(rate)), time)
                        print(f"At the end of {time} years your total amount will be £{float(amount):,.2f}")
                        break

                start_again()
            except ValueError:
                print("Please enter a number for the deposit, interest rate, and years.")
            except TypeError:
                print("Invalid input. Please make sure to enter numbers only.")


    elif option == "2":
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
                print(f"Total of {installments} installments of £{float(repayments):,.2f} ")
                start_again()


            except ValueError:
                print("Please enter house price, interest rate, and number of monthly installments.")
            except TypeError:
                print("Invalid input. Please make sure to enter numbers only.")            


    elif option.lower() == "exit":
        print("Thank you for using our calculator. Goodbye!")
        break
    else:
        print("Invalid option. Please enter a valid option number or 'exit'.")



       


        



