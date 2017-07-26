#-*- coding: utf-8 -*-
import decimal
import math
from decimal import Decimal,getcontext
from decimal import *
print('**********CALCULATING EVERYTHING USING LIBRARY FUNCTIONS**********')
radius_value=input('Enter legal value of the RADIUS:-')
radius_value = Decimal(radius_value)
#radius_value = (radius_value)
if Decimal(radius_value)>100:
    raise ValueError('A very specific bad thing happened')
print('Value of PI using library functions is ')
print(math.pi)
def samesign(a, b):
        return a * b > 0

def bisect(func, low, high):
    'Find root of continuous function where f(low) and f(high) have opposite signs'

    assert not samesign(func(low), func(high))

    for i in range(10):
        midpoint = (low + high) / 2.0
        if samesign(func(low), func(midpoint)):
            low = midpoint
        else:
            high = midpoint

    return midpoint

def f(x1):
    #x1 = Decimal(x1)
    return (x1-(math.sin(x1))-(math.pi/2))

#x1 = Decimal(bisect(f, 1, 3))
x1 = (bisect(f, 1, 3))
print("Value of ANGLE in RADIANS would be ")
print(x1)
#theta_value=Decimal(180*x1/math.pi)
theta_value=(180*x1/math.pi)
print("Value of ANGLE in DEGREEs would be ")
print(theta_value)

print('Value of sine using library functions')
print(math.sin(x1))
print('Value of cosine using library functions')
print(math.cos(x1))
d=Decimal(1-(math.cos(x1/2)))
#d=(1-(math.cos(x1/2)))
print('Value of length segment using library functions')
print ((2*(radius_value)*d))

def valuepassfromlibrary(l):

     l=Decimal(2*(radius_value)*d)