x, op, y = input('Enter x op y (+ - * / ^): ').split()
x, y = int(x), int(y)
if op == '+':
    print(f"{x+y:.4f}")
elif op == '-':
    print(f"{x-y:.4f}")
elif op == '*':
    print(f"{x*y:.4f}")
elif op == '/':
    print(f"{x/y:.4f}")
elif op == '^':
    print(f"{x**y:.4f}")
else:
    print('Invalid op')