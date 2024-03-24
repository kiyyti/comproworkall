cre = int(input("Enter credit card debt: "))
mpay = int(input("Enter credit card debt: "))
x = cre
i = 0
y = 0
while 1:
    y += cre*0.015
    cre = (cre+(cre*0.015))-mpay
    i+=1
    if cre<=0:
        print(f"Month {i} : Debt is paid off")
        break
    print(f"Month {i} : {cre}")
print(f"Total payment = {x+y:.2f}")
    