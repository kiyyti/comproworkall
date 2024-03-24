import math as m
width, height = map(float,input('Enter height and width (cm): ').split())
c_area = m.pi*width**2
t_area = 0.5*width*height
r_area = width*height
s_area = height**2
print(f"Circle area = {c_area:.1f} cm^2")
print(f"Triangle area = {t_area:.3f} cm^2")
print(f"Square area = {s_area:.4f} cm^2")
print(f"Rectangle area= {r_area:.4f} cm^2")