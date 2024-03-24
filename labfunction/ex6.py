#min function
def mymin():
    mi = min(x) 
    return mi

#max function
def mymax():
    ma = max(x)
    return ma

x = input('Enter n nember:').split()

print('Max value =',mymax())
print('Min value =',mymin())