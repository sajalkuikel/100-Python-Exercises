import math
def volume(h,r=10 ):
    p= math.pi
    # r=10
    v=(4 * p * r**3 ) / 3 - (p * h**2 *(3*r-h))/3
    return v

print(volume(2))

