money_owed = float(input("How much money do you owe, in dollars?\n"))
apr = float(input("What is the annual principal rate for the loan?\n"))
payments = float(input("How much will you pay off each months, in dollars?\n"))
months = int(input("How many months you wanna see the result for?\n"))

monthly_rate  = apr/100/12 #with this we can get the monthly rate

for i in range(months):
    #calculate the interest to pay
    interest_paid = money_owed*monthly_rate

    #add in interest
    money_owed = money_owed + interest_paid

    if(money_owed - payments < 0):
        print(f"The last payment is: {money_owed}")
        print(f"You paid the loan in {i+1} months")
        break
    
    #make payments
    money_owed = money_owed - payments

    print(f"Paid {payments} of which {interest_paid} was the interest", end=" ")
    print(f"Now I owe {money_owed} dollars")