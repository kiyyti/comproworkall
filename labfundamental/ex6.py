kun = []
ac = int(input('Actual fixed cost: '))
for i in range(1,4):
    k = int(input(f'Night{i}: How many cars? '))
    kun.append(k)

print(f'Expected fixed cost: {(((120-(120*(20/100)))*30)*3 ):.2f} Baht')
print(f'Revenue = {sum(kun)*30:.2f} Baht')
print(f'profit = {sum(kun)*30-ac:.2f} Baht')