def leaky_reluto(x,a):
    if x>=0:
        return x
    else:
        answer = x*a
        return answer
r = leaky_reluto(-10,0.005)
print(r)