import math as m
x1, y1, x2, y2 = map(int,input("Enter x1, y1, x2, y2: ").split())

#function Manhattan
def Manhattan_distance():
    mand = m.sqrt((x1-x2)**2+(y1-y2)**2)
    return mand

#fjnction Euclidean
def Euclidean_distance():
    eud = abs(x1 - x2) + abs(y1 - y2)
    return eud

print(f"Manhattan distance = {Euclidean_distance():.4f}") 
print(f"Euclidean distance = {Manhattan_distance():.4f}")