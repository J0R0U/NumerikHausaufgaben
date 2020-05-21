# -*- coding: utf-8 -*-

from numpy import array, linalg
from math import sin, cos, exp

def newton(x_0, f, f_derative_inverse):
    x = x_0
    
    for i in range(0,1001):
        x = x - f_derative_inverse(x).dot(f(x))
    
    return x

def f(vec):
    x = vec[0]
    y = vec[1]
    
    matrix = array([
        sin( x) - y,
        exp(-y) - x
    ])
    
    return matrix

def f_derative_inverse(vec):
    x = vec[0]
    y = vec[1]
    
    factor = 1 / (-cos(x) * exp(-y) - 1)
    
    matrix = array([
        [-exp(-y),      1],
        [       1, cos(x)]
    ])
    
    return factor * matrix

x_0 = array([
    0,
    0
], dtype=float)

ret = newton(x_0, f, f_derative_inverse)
print(ret)