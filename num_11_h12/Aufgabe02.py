# -*- coding: utf-8 -*-

from math import sin, pi
from scipy import integrate

def f(x):
    return sin(pi * x ** 2)

def calc_integral(f, i, a, b, o):
    calc_trapezoid = lambda intervall_len, x, y: 1 / 2 * (x + y) * intervall_len
    
    intervall_len = i(a, b, o)
    intervall_count = (int)((b - a) / intervall_len);
    
    values = [f(a + i * intervall_len) for i in range(0, intervall_count + 1)]
    
    return sum([calc_trapezoid(intervall_len, values[i], values[i + 1]) for i in range(0, len(values) - 1)])

def romberg_intervall_len(a,b,o):
    if o == 0:
        return b - a
    else:
        return romberg_intervall_len(a, b, o - 1) / 2

def bulirsch_intervall_len(a,b,o):
    if o > 2:
        return bulirsch_intervall_len(a, b, o - 2) / 2
    elif o == 2:
        return (b - a) / 3
    elif o == 1:
        return (b - a) / 2
    elif o == 0:
        return b - a
    

a = -1
b = 1
o_s = [2,4,6,8,10,12,14,16]
    
for o in o_s:
    print("o =", o, ":")
    print(" Romberg:  ", calc_integral(f, romberg_intervall_len, a, b, o))
    print(" Bulirsch: ", calc_integral(f, bulirsch_intervall_len, a, b, o))
    print(" quad:     ", integrate.quad(f, a, b)[0])