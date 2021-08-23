import math

def find_roots(a, b, c):
     delta = (b**2) - (4*a*c)
     # find two solutions
     s1 = (-b-math.sqrt(delta))/(2*a)
     s2 = (-b+math.sqrt(delta))/(2*a)
     return s1,s2

print(find_roots(2, 10, 8));