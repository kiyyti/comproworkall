import math as m
x1, y1, x2, y2 = map(int,input("Enter x1, y1, x2, y2: ").split())
eu = m.sqrt((x1-x2)**2+(y1-y2)**2)
man = abs(x1 - x2) + abs(y1 - y2)
print(f"Euclidean distance = {eu:.6f}")
print(f"Manhattan distance = {man:.6f}") 