tlate = int(input('How many hours do you submit late? '))

score = int(input('\nWhat is your estimated score? '))

if tlate == 0:
    print(f'Your expected score is {score:.1f}')
elif tlate <= 24:
    print(f'Your expected score is {score-(score*0.2):.1f}')
elif tlate <= 48:
    print(f'Your expected score is {score-(score*0.50):.1f}')
elif tlate > 48:
    print(f'Your expected score is {score-score:.1f}')