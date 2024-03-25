td = {}

while 1:
    tds = input('To do: ')
    if tds == '':
        break

    td[tds] = input('* details: ')

tdss = sorted(td.items())    

for i in tdss:
    print(i[0])
    print(f"* details: {i[1]}")
