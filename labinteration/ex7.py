k = int(input('Input number of value(s): '))
m = []
n = 0
if k == 1:
    a = float(input(''))
    print(f"Weighted Avg = {a:.4f}")
else:
    # lish(mx) to lish(m)
    mx = input('').split()
    for i in range(len(mx)):
        m.append(int(mx[i]))
    print(m)
    m1 = m[0]
    for j in range(2,k+1):
        m[j] = (m[j-2]*(j-1)+j)/j
        print(m[j])
    print(f'Weighted Avg = {n:.5f}')