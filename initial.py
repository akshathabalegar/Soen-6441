'''
Created on Jul 23, 2017

@author: Akshatha
'''
from decimal import Decimal,getcontext
#from test.test_functools import Decimal 
#import Decimal *
#from Decimal import *
import math
#from hites import import *
#from future_builtins import *
#from Tkinter import *

#root = Tk()
#root.title("HITES")
#root.geometry("900x500")
#root.mainloop()
#quitButton=Button("CLICK ME")
#quitButton.place(x=0,y=0)
#import math

#Sets decimal to 50 digits of precision
getcontext().prec = 7

def caluclating_factorial(n_val):
    if n_val<1:
        return 1
    else:
        return n_val * caluclating_factorial(n_val-1)

def calculating_pi(n_val):   #plouffbig
    pi_val = Decimal(0)
    i = 0
    while i < n_val:    
        pi_val += (Decimal(1)/(16**i))*((Decimal(4)/(8*i+1))-(Decimal(2)/(8*i+4))-(Decimal(1)/(8*i+5))-(Decimal(1)/(8*i+6)))
        i += 1
    return pi_val

