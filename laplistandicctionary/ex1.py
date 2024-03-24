v1 = [float(x) for x in input('Enter values of the vector: ').split()]
v2 = [float(y) for y in input('Enter values of the vector: ').split()]
print("v1:",v1)
print("v2:",v2)
v3 = []
for i in range(len(v1)):
    v3.append(v1[i]+v2[i])
print('v1 +v2 =',v3)    