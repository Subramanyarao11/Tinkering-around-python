total = 0
expenses = []

for i in range(7):
    expenses.append(float(input("Enter the Expense:")))

total = sum(expenses)

print("You spent $", total, sep='')
