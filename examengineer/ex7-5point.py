a = input('Is it raining? (yes/no):')
tem = int(input('Temperature (C): '))
wind = int(input('Wind speed (km/hr): '))
if a == 'yes':
    print('We will NOT play basketball.')
else:
    if tem > 35 or wind > 5:
        print('We will NOT play basketball.')
    else:
        print('We will play basketball.')