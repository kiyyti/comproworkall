fp = int(input('Food price: '))
dp = int(input('Drink price: '))
print(f"Total Price = {fp+dp} Bath")
print(f"Discount after check-in = {(fp+dp)-(fp+dp)*(5/100)} Bath")
print(f"If you are a member, you would pay {(fp+dp)-(fp+dp)*(10/100)} Bath")