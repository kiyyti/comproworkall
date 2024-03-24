psum = 0
p= 0
nsum = 0
n = 0
while 1:
    x = int(input("Enter a number (0 to quit): "))
    if x == 0:
        break
    elif x > 0:
        psum += x
        p += 1
    elif x < 0:
        nsum += x
        n += 1
print(f"Pos: sum = {psum:.2f} Avg = {psum/p}") 
print(f"Neg: sum = {nsum:.2f} Avg = {nsum/n}") 