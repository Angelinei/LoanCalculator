Loan = int(input("Enter the loan amount: "))
Interest = float(input("Enter the interest rate: "))
Years = int(input("Enter the number of years: "))
print("Year\tAmount")
for i in range(1, Years + 1):
    Amount = Loan * (1 + Interest) ** i
    print(i, "\t", Amount)