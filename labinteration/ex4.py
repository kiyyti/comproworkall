x = int(input("Enter n: "))
i = 1
sum = 0
while 1:
    sum += 1/i
    print(f"Round {i} : sum = {sum:.5f}")
    i += 1
    if sum > x:
        break