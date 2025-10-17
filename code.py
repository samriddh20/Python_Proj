class loan_cal:
    def __init__(self, withdrawn_amount, apr):
        self.money = withdrawn_amount
        self.apr = apr
    
    def showDetails(self):
        print(f"You have taken a loan of {self.money} dollars at {self.apr}% annual principal interest rate.")
    
    def loan_status(self):
        payment = float(input("How much will you pay off each months, in dollars?\n"))
        months = int(input("How many months you wanna see the result for?\n"))

        monthly_rate = self.apr/100/12

        for i in range(months):
            #calculate the interest to pay
            interest_paid = self.money*monthly_rate

            #add in interest
            self.money = self.money + interest_paid

            if(self.money - payment < 0):
                print(f"The last payment is: {self.money}")
                print(f"You paid the loan in {i+1} months")
                break
            
            #make payments
            self.money = self.money - payment

            print(f"Paid {payment} of which {interest_paid} was the interest", end=" ")
            print(f"Now I owe {self.money} dollars")

a = loan_cal(50000, 3)
a.showDetails()
a.loan_status()