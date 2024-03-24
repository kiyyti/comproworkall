print("Hi! I am a smart cashier!")
fc = int(input('Enter the food cost: '))
ay = int(input('Enter the amount you pay: '))
t = ay-fc
i1000 = 0
i500 = 0
i100 = 0
i50 = 0
i20 = 0
i10 = 0
i5 = 0
i1 = 0
print(f"\nAmount of change =  {t}")
while 1:
    if t>=1000:
        t -= 1000
        i1000 += 1
    elif t>=500:
        t -= 500
        i500 += 1
    elif t>=100:
        t -= 100
        i100 += 1
    elif t>=50:
        t -= 50
        i50 += 1
    elif t>=20:
        t -= 20
        i20 += 1
    elif t>=10:
        t -= 10
        i10 += 1
    elif t>=5:
        t -= 5
        i100 += 1
    elif t>=1:
        t -= 1
        i100 += 1
    else:
        break
print(f"\t{i1000}\t1000-Baht bill(s)")
print(f"\t{i500}\t500-Baht bill(s)")
print(f"\t{i100}\t100-Baht bill(s)")
print(f"\t{i50}\t50-Baht bill(s)")
print(f"\t{i20}\t20-Baht bill(s)")
print(f"\t{i10}\t10-Baht bill(s)")
print(f"\t{i5}\t5-Baht bill(s)")
print(f"\t{i1}\t1-Baht bill(s)")
