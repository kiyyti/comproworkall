items = []
prices = []
shopping = {}
while 1:
    x,y = 0,0
    x,y = input('Item and price to buy:').split()
    if x == 'no' and y == "more":
        break
    items.append(x)
    prices.append(int(y))
print("print(items)")
print(items)
print("print(prices)")
print(prices,"\n")
print("Items purchased:")
for item , price in zip(items, prices):
    shopping[item] = price
print("\nShopping List:")
print(shopping) 
