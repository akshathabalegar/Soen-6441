#-*- coding: utf-8 -*-
from decimal import Decimal,getcontext
from decimal import *
from xml.etree.ElementTree import Element,ElementTree, tostring
import math
import sys
from xml.etree import ElementTree as ET
import xml.dom.minidom as MD   
# import pdb
# pdb.set_trace()
getcontext().prec = 7
print('**********CALCULATING EVERYTHING FROM SCRATCH**********')
def caluclating_factorial(number_value):   #RECURSION is used for calculating FACTORIAL from SCRATCH
    if number_value<1:
        return 1
    else:
        return number_value * caluclating_factorial(number_value-1)

def calculating_pi(number_value):     #The Bailey–Borwein–Plouffe formula (BBP formula) for calculating PI value from SCRASTCH
    pi_value = Decimal(0)
    i = 0
    while i < number_value:
        pi_value += (Decimal(1)/(16**i))*((Decimal(4)/(8*i+1))-(Decimal(2)/(8*i+4))-(Decimal(1)/(8*i+5))-(Decimal(1)/(8*i+6)))
        i += 1
    return pi_value

def calculating_sine(theta_value):    #The Taylor Series for calculating sin(x) from SCRATCH
    x_value=theta_value
    m=0

    for k in range(0,10,1):
        y=(((-1)**k)*(x_value)**(1+(2*k)))/(caluclating_factorial(1+(2*k)))
        m+=y

    return m

def calculating_cosine(theta_value):     #The Taylor Series for calculating cos(x) from SCRATCH
    x_value=theta_value
    m=0
    
    for k in range(0,10,1):
        y=((-1)**k)*(x_value**(2*k))/caluclating_factorial(2*k)    #Taylor Expansion of Cosine
        m+=y
    return m

for j in range(1,3):
    pi_value=calculating_pi(2)
    
print("Value of PI would be: ")
print(pi_value)

def samesign(a, b):
        return a * b > 0

def bisect(func, low, high):    #The Bisection Method for calculating ROOT of the equation from SCRATCH
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
    x1 = Decimal(x1)
    return x1-calculating_sine(x1)-(pi_value/2)

x1 = Decimal(bisect(f, 1, 3))
print("Value of ANGLE in RADIANS would be ")
print(x1)
theta_value=Decimal(180*x1/pi_value)
 
print("Value of ANGLE in DEGREEs would be ")
print(theta_value)

print("Value of sine would be: ")
print(calculating_sine(x1))

print("Value of cosine would be: ")
print((calculating_cosine(x1)))

radius_value=input('Enter legal value of the RADIUS:-')

radius_value = Decimal(radius_value)
if radius_value>100:
    raise ValueError('Please enter the legal value')

linesegment_value=2*(radius_value)*(1-(calculating_cosine(x1/2)))
print("Value of LINE SEGMENT l would be: ")
print(linesegment_value)

#GENERATING THE TEXT FILE FOR ALL OUTPUT VALUES
file_open = open("Incarnation_one_TEXTFILE.txt", "a")
file_open.write("\n")
file_open.write ("For Radius Value "+str(radius_value))
file_open.write("\n")
file_open.write ("Value of the sine using functions from scratch would be "+str(calculating_sine(x1)))
file_open.write("\n")
file_open.write ("Value of the cosine using functions from scratch would be "+str(calculating_cosine(x1)))
file_open.write("\n")
file_open.write ("Value of the angle using functions from scratch in degree would be "+str(theta_value))
file_open.write("\n")
file_open.write ("Value of line segment using functions from scratch would be "+str(linesegment_value))
file_open.write("\n")