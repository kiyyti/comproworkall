favac = input('What is your most favorite activity?')
favmo = input('What kind of activities do you do most?')
favth = input('In your opinion, what kind of activities is the most beneficial?')
if favac == favmo != favth:
    print('You are lucky.')
elif favac == favth != favmo:
    print('You are smart.')
elif favmo == favth != favac:
    print('Good for you.')
elif favac == favmo  == favth:
    print('You are blessed.')
else: print('Oh, sorry for that.')