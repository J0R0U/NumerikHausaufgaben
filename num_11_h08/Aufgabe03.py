# -*- coding: utf-8 -*-

from numpy import array, linalg
from math import sin, cos, exp

def newton(x_0, f, f_derivative):
    x = x_0
    
    for i in range(0,1000):
        x = x - linalg.inv(f_derivative(x)).dot(f(x))
    
    return x

def f(x):
    return array([
        sin(x[0])-x[1],
        exp(x[1])-x[0],
    ])

def f_derative(x):
    return array([
        [cos(x[0]), -1         ],
        [-1,        -exp(-x[1])]
    ])



x_0 = array([
    -20,
    -20
], dtype=float)

ret = newton(x_0, f, f_derative)
print(ret)