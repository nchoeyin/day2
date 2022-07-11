def tip_calculator():
    print("Welcome to the tip calculator")
    bill = float(input("Enter the total bill: "))
    percent = int(input("What percent would you like to give tip? 10 or 12 or 15"))
    numOfPeople = int(input("How many people to split the bill: "))
    totalbill = percent / 100 * bill + bill
    perPay = totalbill/numOfPeople
    print("Each individual has to pay {:0.2f}".format(perPay))
    
tip_calculator()
'''
Output: 
Welcome to the tip calculator
Enter the total bill: 10000
What percent would you like to give tip? 10 or 12 or 1510
How many people to split the bill: 2
Each individual has to pay 5500.00
'''
