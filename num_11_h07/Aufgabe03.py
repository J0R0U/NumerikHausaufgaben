# -*- coding: utf-8 -*-

from numpy import finfo
from math import exp

def newton(x_0, f, f_derivative, e):
    n = 0
    
    x = x_0
    current_e = finfo(float).max
    
    while current_e > e:
        x_new = x - f(x) / f_derivative(x)
        
        current_e = abs(x - x_new)
        
        x = x_new
        n += 1
        
    return x, n

def sekanten(x_0, x_1, f, e):
    n = 0
    
    x_before  = x_0
    x_current = x_1
    
    f_before  = f(x_before)
    
    while abs(x_before - x_current) > e:
        f_current = f(x_current)
        
        x_new = x_current - ((x_current - x_before) / (f_current - f_before)) * f_current
        
        x_before  = x_current 
        x_current = x_new
        
        f_before = f_current;
        n += 1
    return x_current, n

def f(x):
    a = 9.8606
    c = -1.1085 * 10 ** 25
    d = 0.029
    
    return a / (1 - c * exp( -d * x ) ) - 9

def f_derivative(x):
    a = 9.8606
    c = -1.1085 * 10 ** 25
    d = 0.029
    
    return -(a * c * d * exp( d * x )) / (exp( d * x ) - c) ** 2

e = 2**-24

val , n = newton(1961, f, f_derivative, e)
print('newton:')
print('  n:   ', n)
print('  val: ', val)

val , n = sekanten(1961, 2000, f, e)
print('sekanten:')
print('  n:   ', n)
print('  val: ', val)



