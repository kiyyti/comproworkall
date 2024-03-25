td = {}

while 1:
    tds = input('To do: ')
    if tds == '':
        break

    td[tds] = input('* details: ')

tdss = sorted(td.items())    

print(f'You have  {len(tdss)} thing(s) to do: ')
for i in tdss:
    print("*",i[0])

q = input("Command (enter name for details or 'all' for everything): ")
for kitti in td.keys():
    if q == kitti:
        kit = kitti
if q == "all":
    for i in tdss:
        print("*",i[0])
        print(f"** details: {i[1]}")
    print('Bye')
elif q == kit:
    print("*",q)
    print("**",td.get(q))
    print('Bye')
else:
    print("Bye")
    
