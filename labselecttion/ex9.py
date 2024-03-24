product = []
price = []
for i in range(3):
    pu,pi = input('Enter product and price: ').split()
    product.append(pu)
    price.append(int(pi))

print('\n------ Receipt ------')
print('Item',end="\t\t\t")
print('Price')
print(product[0],end="\t\t\t")
print(f"{price[0]:.2f}")
print(product[1],end="\t\t\t")
print(f"{price[1]:.2f}")
print(product[2],end="\t\t\t")
print(f"{price[2]:.2f}")

total = 0
prinotax = 0
taxto = 0
for i in range(3):
    total += price[i]
    if product[i][0] == 'T':
        st = price[i]*100/107
        tax = price[i] - st
        taxto += tax
        prinotax += st
    elif product[i][0] != 'T':
        prinotax += price[i]
print(f"\nTotal =\t\t     {total:.2f}")
print(f"Price with no tax =  {prinotax:.2f}")
print(f'Total tax =\t     {taxto:.2f}')
