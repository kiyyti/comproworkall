def readinput(x,y,z):
    num3 = []
    num3.append(float(x))
    num3.append(float(y))
    num3.append(float(z))
    num3.sort()    
    return num3
x, y, z = map(float,input('Enter 3 numbers: ').split())

re = readinput(x,y,z)
print(re[0], '<=', re[1], '<=', re[2])