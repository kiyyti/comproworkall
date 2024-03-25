import math
x = int(input('Number of values:'))
rms = 0
for i in range(x):
    y = float(input('value:'))
    rms += y**2
rms = math.sqrt(rms/x)
print('RMS = {:,.2f}'.format(rms))