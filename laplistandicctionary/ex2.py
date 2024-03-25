row, col = map(int,input('Enter 2D list size (row,col): ').split())

rows = []

for i in range(row):
    ro = [int(x) for x in input(f'Enter {col} integers for row {i}: ').split()]
    rows.append(ro)

print("In order:")
for r in rows:
    for rs in r:
        print(f'{rs}',end="\t")
    print()

print("Reverse col, same row:")
for t in rows:
    t.reverse()
    for rs in t:
        print(f'{rs}',end="\t")
    print()

print("Same col, reverse row:")
for t in rows[::-1]:
    t.reverse()
    for rs in t:
        print(f'{rs}',end="\t")
    print()

print("Reverse col, reverse row:")
for t in rows[::-1]:
    t.reverse()
    for rs in t:
        print(f'{rs}',end="\t")
    print()