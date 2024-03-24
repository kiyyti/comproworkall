pu, pi = input('Enter product and price: ').split()
pi = int(pi)

if pu[0] != 'T':
    print(f'Price without tax = {pi:.2f} Baht')
    print(f'7% Tax = 0.00 Baht')
elif pu[0] == 'T':
    st = pi*100/107
    tax = pi - st
    print(f'Price without tax = {st:.2f} Baht')
    print(f'7% Tax = {tax:.2f} Baht')