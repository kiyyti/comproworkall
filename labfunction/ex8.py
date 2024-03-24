# function input income
def rdIncome():
    income = float(input("Enter your income (Baht): "))
    if income > 0:
        return income
    else:
        return None
    
income = rdIncome()

# function check income
def isValid(income):
    if income is None:
        return False
    elif income > 1000000:
        return False
    else:
        return income

# function calculate tax
def comptax():
    if 0 <= isValid(income) <= 150000:
        return 0
    elif 150000 < isValid(income) <= 500000:
        return (isValid(income) - 150000) * 0.1
    elif 500000 < isValid(income) <= 1000000:
        return 35000 + (isValid(income) - 500000) * 0.2

print(f'Income: {isValid(income):.0f}')
if isValid(income) > 0:
    print(f'Tax: {comptax():.0f}')
else:
    print('Invalid income.')