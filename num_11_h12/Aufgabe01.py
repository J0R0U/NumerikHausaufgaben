# -*- coding: utf-8 -*-

from math import sqrt
from numpy import arctan

def exact_integral(a, b):
    return arctan(b) - arctan(a)

def summed_trapezoid(a, b):
    f = lambda x: 1 / (1 + x**2)
    calc_trapezoid = lambda intervall_len, x, y: 1 / 2 * (x + y) * intervall_len
    
    intervall_count = 8
    intervall_len = (b - a) / intervall_count
    
    values = [f(a + i * intervall_len) for i in range(0, intervall_count + 1)]
    
    return sum([calc_trapezoid(intervall_len, values[i], values[i + 1]) for i in range(0, len(values) - 1)])

def summed_simpson(a, b):
    f = lambda x: 1 / (1 + x**2)
    calc_simpson = lambda intervall_len, a, b: 1 / 6 * (f(a) + 4 * f((a + b) / 2) + f(b)) * intervall_len
    
    intervall_count = 4
    intervall_len = (b - a) / intervall_count
    
    values = [a + i * intervall_len for i in range(0, intervall_count + 1)]
    
    return sum([calc_simpson(intervall_len, values[i], values[i + 1]) for i in range(0, len(values) - 1)])

def gauss_integration(a, b):
    f = lambda x: 1 / (1 + x**2)
    
    x_s = [(b - a) / 2 * x + (b + a) / 2 for x in [-sqrt(3 / 5), 0, sqrt(3 / 5)]]
    beta_s = [(b - a) / 2 * beta for beta in [5 / 9, 8 / 9, 5 / 9]]
    
    return sum([beta_s[i] * f(x_s[i]) for i in range(0, 2)])

a = 0
b = 1

exact_integral = exact_integral(a, b)
summed_trapezoid = summed_trapezoid(a, b)
summed_simpson = summed_simpson(a, b)
gauss_integration = gauss_integration(a, b)

print("exact:            ", exact_integral)
print("summed_trapezoid: ", summed_trapezoid, "(", exact_integral - summed_trapezoid, ")")
print("summed_simpson:   ", summed_simpson, "(", exact_integral - summed_simpson, ")")
print("gauss_integration:", gauss_integration, "(", exact_integral - gauss_integration, ")")