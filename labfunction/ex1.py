import math as m
def convert_rec_pol(real,imaginary):
    mag = m.sqrt(real**2 + imaginary**2)
    phase = m.atan(imaginary/real) 
    return mag,phase
mag, phase = convert_rec_pol(1,3**0.5)
print(mag,phase)