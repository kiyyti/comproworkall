x,a,y=map(str,input('Enter x op y (+ - * / // %): ').split())
if x == "0" and y == "0":
    print("Bye!.")
elif a == "-":
    print(f'{float(x):.2f} - {float(y):.2f} =',float(x)-float(y))
elif a == "+":
    print(f"{float(x):.2f} + {float(y):.2f} =",float(x)+float(y))
elif a == "*":
    print(f"{float(x):.2f} * {float(y):.2f} =",float(x)*float(y))
elif a == "/":
    print(f"{float(x):.2f} / {float(y):.2f} =",float(x)/float(y))
elif a == "//":
    print(f"{int(x):.2f} // {int(y):.2f} =",float(x)//float(y))
elif a == "%":
    print(f"{int(x):.2f} % {int(y):.2f} =",float(x)%float(y))
else:
    print("Wrong op.")