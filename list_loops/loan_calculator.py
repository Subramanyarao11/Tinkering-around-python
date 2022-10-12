# Get the loan details
money = float(input("How much money do you owe, in dollars?\n"))
interest = float(input("What is the Rate of Interest?\n"))
payment = float(input("Monthly Payment, in dollars\n"))
months = int(input("How many months do you want to see results for?\n"))


# Divide interest by 100 to make it in terms of percentage , then dividing it by 12 to get montly interest

monthly_interest = interest/100/12


for i in range(months):
    # Adding Interest

    interest_paid = money * monthly_interest
    money = money + interest_paid


    if(money - payment < 0):
        print("The last payment is",round(money,2))
        print("You Paid off loan in",i+1,"months")
        break


    # Make Payment

    money = money - payment

    # Printing the results after every month

    print("Paid", payment,"$", "of which", round(interest_paid , 2), "$", "was interest", end=' ')
    print("Now I Owe", round(money,2),'$')
