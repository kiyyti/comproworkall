n = int(input('Please enter a vector length, n : '))
vec = input('Enter values of the vector: ').split()

vector = []

for i in vec:
    vector.append(float(i))

if len(vector) == n:
    print(f'Vector:\n{vector}')
else:
    print(f'Expect {n} values. Found {vector} .')