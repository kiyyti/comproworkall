Tax = input('Net Income: ')
if Tax == 'q' or Tax == 'Q':
    print('Bye')
else:
    Taxs = int(Tax)
    if Taxs < 0:
        print('Wrong input: negative income.')
    elif Taxs <= 150000:
        tax = 0
        print(f'Tax = {tax:.2f} Baht.')
    elif Taxs <= 300000:
        tax = (Taxs - 150000) * 0.05
        print(f'Tax = {tax:.2f} Baht.')
    elif Taxs <= 500000:
        tax = 7500 + (Taxs - 300000) * 0.10
        print(f'Tax = {tax:.2f} Baht.')
    elif Taxs <= 750000:
        tax = 27500 + (Taxs - 500000) * 0.155
        print(f'Tax = {tax:.2f} Baht.')
    elif Taxs <= 1000000:
        tax = 65000 + (Taxs - 750000) * 0.20
        print(f'Tax = {tax:.2f} Baht.')
    elif Taxs <= 2000000:
        tax = 115000 + (Taxs - 1000000) * 0.30
        print(f'Tax = {tax:.2f} Baht.')
    elif Taxs <= 5000000:
        tax = 365000 + (Taxs - 2000000) * 0.30
        print(f'Tax = {tax:.2f} Baht.')
    else:
        tax = 1265000 + (Taxs - 5000000) * 0.35
        print(f'Tax = {tax:.2f} Baht.')