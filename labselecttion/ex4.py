rain = input('Is it raining? (Yes/No): ')
hum = int(input('Humidity (0-100): '))
vspeed = int(input('Wind speed (km/hr): '))

rains = rain.lower()

if rains == "yes":
    print('We will NOT play tennis.')
elif rains == 'no':
    if hum > 65 or  vspeed > 5:
        print('We will NOT play tennis.')
    else:
        print('We will PLAY tennis.')