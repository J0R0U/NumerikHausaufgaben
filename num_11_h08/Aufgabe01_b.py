# -*- coding: utf-8 -*-

from numpy import arctan, array

def newton(x_0, f, f_derivative):
    ret = [x_0]
    x = x_0
    
    for i in range(0,4):
        x =  x - f(x) / f_derivative(x)
        ret.append(x)
    
    return ret

def variant_1(x_0, f, f_derivative, q):
    ret = [x_0]
    x = x_0
    
    for i in range(0,4):
        x =  x - q * f(x) / f_derivative(x)
        ret.append(x)
    
    return ret


def variant_2(x_0, f, f_derivative, f_second_derivative):
    ret = [x_0]
    x = x_0
    
    for i in range(0,4):
        x =  x - ( f(x) * f_derivative(x) ) / f_derivative(x) ** 2 - f(x) * f_second_derivative(x)
        ret.append(x)
    
    return ret

def f(x):    
    return arctan(x) - x

def f_derivative(x):
    return 1 / ( x ** 2 + 1) - 1

def f_second_derivative(x):
    return -2 * x / (x ** 2 + 1) ** 2

data = array ([
    newton(1, f, f_derivative),
    variant_1(1, f, f_derivative, 1),
    variant_2(1, f, f_derivative, f_second_derivative)
])

data = data.transpose()

print(data)
