print('Thip! Thip Thip!')

place = []
numtra = int(input('\nNumber of travelers: '))
print('Where will your visit?')
for i in range(1,4):
    places = input(f'Place {i}: ')
    place.append(places)

print()

dit1 = int(input(f'Distance form home to {place[0]}: '))
dit2 = int(input(f'Distance form {place[0]} to {place[1]}: '))
dit3 = int(input(f'Distance form {place[1]} to {place[2]}: '))
dit4 = int(input(f'Distance form {place[2]} to home: '))

gasco = int(input('\nGas cost per km (Baht): '))
numday = int(input('Number of days: '))
numnight = int(input('Number of nights: '))
horate = int(input('Hotel rate: '))

print('\n---- Your trip info ----')

distanto = dit1+dit2+dit3+dit4
hocost = horate*numnight
print(f'Total distance = {distanto:.1f}')
print(f'Total gas cost = {distanto*gasco:.1f}')
print(f'Total hotel cost = {hocost:.1f}')
print(f'Total shared cost = {(distanto*gasco)+(hocost):.1f}')
print(f'Food cost per person = {150*numday:.1f}')
print(f'Total cost per person = {((distanto*gasco)+(hocost)+(150*numday))/numtra:.1f}')