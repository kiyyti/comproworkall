row, col = map(int,input('Enter 2D list size (row,col): ').split())

rows = []
for i in range(row):
    ro = input(f'Enter 5 integers for row {i}: ').split()
    rows.append(ro)
print(rows[1])