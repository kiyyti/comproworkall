import math as m
#funtion input 4 number
num = []
def read():
    while 1:
        if len(num) == 4 :
            break
        x = int(input('Please enter a positive integer:'))
        if x <= 0:
            print('Invalid input value. Please try again.')
        elif x > 0:
             num.append(x)
    return num

b = read()

#function calculater for find z
def findPower():
    z = m.sqrt((b[0]**b[1]+b[1]**b[2]+b[2]**b[3])/10.25)
    return z

print(f'z = {findPower():.6f}')