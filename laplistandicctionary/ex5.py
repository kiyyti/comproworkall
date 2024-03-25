s = int(input('Enter a size: '))
v = input('Enter 10 integers: ').split()
x = []

for i in v:
    x.append(int(i))

a = sorted(x)
b = reversed(a)

print(f"In order:")
for i in a:
    print(i,end=" ")

print('\nReverse order:')
for j in b:
    print(j,end=" ")
