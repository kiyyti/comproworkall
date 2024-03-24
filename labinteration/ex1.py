x = int(input('Enter n: '))
for i in range(1,x+1):
    if i % 10 == 0:
        print("x")
        continue
    if i % 5 == 0 :
        print("x",end=" ")
        continue
    print(i,end=" ")