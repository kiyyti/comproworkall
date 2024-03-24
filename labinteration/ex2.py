x = int(input("Enter n: "))
for i in range(x):
    if i % 5 == 0:
        print('!',end=(""))
    else:
        print("*",end=(""))