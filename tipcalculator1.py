def tip_calculator():
    print("Welcome to the tip calculator")
    bill = float(input("Enter the total bill: "))
    percent = int(input("What percent would you like to give tip? 10 or 12 or 15"))
    numOfPeople = int(input("How many people to split the bill: "))
    totalbill = percent / 100 * bill + bill
    perPay = totalbill/numOfPeople
    pay = round(perPay, 2)
    print(f"Each individual has to pay {pay}")
tip_calculator()
