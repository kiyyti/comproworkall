import random as r

# funtion random number ai
def checkLottery():
    y = r.randint(10,99)
    return y

# function input number for user 
def getinput():
    while 1:
        x = input('Enter a 2-digit number: ')
        if x[0] != '0' and len(x) == 2:
            break
    return x
funcin = getinput()

if 10 <= int(funcin) <= 10:
    print('Almost got it')
    print(f'lottery number = {checkLottery()}')
elif int(funcin) == checkLottery():
    print('Congratulations!')
    print(f'lottery number = {checkLottery()}')
else:
    print('No, sorry :(')
    print(f'lottery number = {checkLottery()}')