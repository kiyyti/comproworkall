net_income = int(input("Net Income: "))
if net_income == "q":
    print("Bye")
elif net_income < 0:
    print("Wrong input: negative income.")
elif net_income <=150000:
    print("Tax = 0.00 Baht")
elif net_income > 150000:
    if net_income <= 300000:
        tax = (net_income-150000) * 0.05
        print(net_income)
    elif net_income <= 500000:
        tax = (net_income-150000) * 0.1
    elif net_income <= 750000:
        tax = (net_income-150000) * 0.15
    elif net_income <= 1000000:
        tax = (net_income-150000) * 0.20
    elif net_income <= 2000000:
        tax = (net_income-150000) * 0.25
    elif net_income <= 5000000:
        tax = (net_income-150000) * 0.30
    else:
        tax = (net_income-150000) * 0.35
print(tax)