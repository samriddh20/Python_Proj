
class LoanCalculator:
    def __init__(self, principal, apr):
        self.principal = principal  # Total amount borrowed
        self.apr = apr              # Annual interest rate (%)
        self.monthly_rate = apr / 100 / 12  # Derived value, can be reused

    def show_details(self):
        print(f"You have taken a loan of ${self.principal:.2f} at {self.apr}% annual interest rate.\n")

    def calculate_loan(self, monthly_payment, months):
        money_owed = self.principal

        for month in range(1, months + 1):
            # Calculate monthly interest
            interest_paid = money_owed * self.monthly_rate

            # Add interest to balance
            money_owed += interest_paid

            if money_owed - monthly_payment < 0:
                print(f"\nFinal payment: ${money_owed:.2f}")
                print(f"Loan paid off in {month} months!")
                break

            # Subtract payment
            money_owed -= monthly_payment

            print(f"Month {month}: Paid ${monthly_payment:.2f} "
                  f"({interest_paid:.2f} interest), Remaining: ${money_owed:.2f}")

        else:
            # If loop completes without break
            print(f"\nAfter {months} months, you still owe ${money_owed:.2f}")

# ---- Example Usage ----
loan = LoanCalculator(50000, 3)
loan.show_details()
loan.calculate_loan(monthly_payment=1000, months=60)
