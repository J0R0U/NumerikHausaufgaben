# -*- coding: utf-8 -*-

from numpy import finfo
from math import log

def newton(x_0, f, f_derivative, e, a):
    x = x_0
    current_error = finfo(float).max
    
    while current_error > e:
        x_new = x - f(x) / f_derivative(x)
        
        current_error = (a / (1 - a)) * abs(x_new - x);
        x = x_new
        
    return x

def f(x):    
    return x + log(x) - 2

def f_derivative(x):
    return 1 + 1 / x

e = 10**-6
a = 1/4

val = newton(1, f, f_derivative, e, a)
print('newton:')
print('  val: ', val)



