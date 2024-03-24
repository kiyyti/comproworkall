name = []
point = []
ss = {}
for i in range(10):
    names, points = input("Enter name and score: ").split()
    name.append(names)
    point.append(int(points))
print('--------------------')
for n,p in zip(name,point):
    ss[n] = p
sss = sorted(ss.items())
print('Sorted student data:')
for i in range(10):
    print(f'{sss[i][0]}\t{sss[i][1]:.2f}')
print('--------------------')
max_p = max(ss.values())
min_p = min(ss.values())
passstu = [k for k, v in ss.items() if v >= 50]
average = sum(ss.values())/len(ss)
averagestu = [k for k, v in ss.items() if v >= average]
print(f'Student(s) with max score of {max_p:.2f}: {", ".join([k for k, v in ss.items() if v == max_p])}')
print(f'Student(s) with min score of {min_p:.2f}: {", ".join([k for k, v in ss.items() if v == min_p])}')
print(f'Student(s) who passes the exam >= 50.00: {", ".join(passstu)}')
print(f'Student(s) who scored at least and above average score of {average:.2f}: {", ".join(averagestu)}')
print('--------------------')
while 1:
    pes = input("Enter your query name: ")
    if pes == "Quit":
        print('Bye')
        break
    else:
        if pes in ss:
            if ss[pes] >= 50:    
                print(f'Score of {pes} is {ss[pes]:.2f}')
                print(f'{pes} has PASSED the exam.')
            else:
                print(f'Score of {pes} is {ss[pes]:.2f}')
                print(f'{pes} has NOT passed the exam.')
        elif pes not in ss:
            print(f"{pes} is not in the database.")