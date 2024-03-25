def leaky_relu(x,y):
    if x >= 0:
        return x
    elif x < 0:
        return y*x


r = leaky_relu(-10,0.005)
print(r)

r = leaky_relu(-10,0.05)
print(r)
    
r = leaky_relu(-2,0.05)
print(r)

r = leaky_relu(0,0.05)
print(r)

r = leaky_relu(2,0.05)
print(r)

r= leaky_relu(10,0.05)
print(r)