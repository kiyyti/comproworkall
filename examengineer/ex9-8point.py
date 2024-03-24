x = int(input('Input first number: '))
y = int(input('Input second number: '))
eiei = []
eiei.append(x)
eiei.append(y)
eieis = sorted(eiei)

op = input('Choose operation (+ or *): ')
od = []
k = 1
if x < y:
    for i in range(x,y+1):
        if i % 2 == 0:
            continue
        else:
            od.append(i)
elif x > y:
    for i in range(y,x+1):
            if i % 2 == 0:
                continue
            else:
                od.append(i)    
if op == "+":
    print(f"Summation of odd number between {eieis[0]} and {eieis[1]} is ",sum(od))    
if op == "*":
    for j in od:
        k *= j
    print(f"Multiplication of odd number between {eieis[0]} and {eieis[1]} is {k}")