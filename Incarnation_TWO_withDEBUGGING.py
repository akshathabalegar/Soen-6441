#-*- coding: utf-8 -*-
import decimal
import math
from decimal import Decimal,getcontext
from decimal import *
from xml.etree.ElementTree import Element,ElementTree, tostring
from xml.etree import ElementTree as ET
import xml.dom.minidom as MD     
from builtins import str
import pdb
pdb.set_trace()
print('**********CALCULATING EVERYTHING USING LIBRARY FUNCTIONS**********')

try:   #EXCEPTION HANDLING
    radius_value=Decimal(input('Enter the Legal value of RADIUS:'))
except ValueError:
    print ("Please enter the valid INPUT")
    
print('Value of PI using library functions is ')
print(math.pi)
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
    return (x1-(math.sin(x1))-(math.pi/2))

x1 = (bisect(f, 1, 3))
print("Value of ANGLE in RADIANS would be ")
print(x1)
theta_value=(180*x1/math.pi)
print("Value of ANGLE in DEGREEs would be ")
print(theta_value)
print('Value of sine using library functions')
print(math.sin(x1))
print('Value of cosine using library functions')
print(math.cos(x1))
d=Decimal(1-(math.cos(x1/2)))
print('Value of length segment using library functions')
print ((2*(radius_value)*d))

#For XML OUTPUT IN THE BROWSER
root=Element('Output')
tree=ElementTree(root)
RadiusValue=Element('Radius')
root.append(RadiusValue)
alphaValue=Element('Alpha')
root.append(alphaValue)
lengthValue=Element('Length')
root.append(lengthValue)
SinValue=Element('Sin')
root.append(SinValue)
CosineValue=Element('Cosine')
root.append(CosineValue)
RadiusValue.text='For Radius : ' + str(radius_value)
SinValue.text='Value of Sine is: ' + str(math.sin(x1))
CosineValue.text='Value of Cosine is: ' + str(math.cos(x1))
alphaValue.text='Value of Angle in DEGREE is: ' + str(theta_value)
lengthValue.text='Value of LENGTH  SEGMENT is : '+ str((2*(radius_value)*d))
tree.write(open('Incarnation_two_XMLFILE.xml', 'wb'))


