from math import sin, cos, exp
from numpy import array, copy, transpose

def infinity_norm(x):
    return max(map(lambda val: abs(val), x))

def calculate_a(p, l, a):
    if(p(a) <= l(a)):
        return a
    else:
        return calculate_a(p, l, 0.5 * a)
    

def steepest_descent(x, f, f_derivative, threshhold):
    x_k = copy(x)
    
    p = lambda val: f(x_k + val * (-f_derivative(x_k)));
    l = lambda val: f(x_k) + 0.5 * transpose(f_derivative(x_k)).dot( -f_derivative(x_k) * val);
    
    while infinity_norm(f_derivative(x_k)) > threshhold:
        x_k = x_k - calculate_a(p, l, 1) * f_derivative(x_k)
    
    return x_k

def f(x):
    return (sin(x[0]) - x[1])**2 + (exp(-x[1])-x[0])**2

def f_derivative(x):
    return array([
        2 * (cos(x[0]) * (sin(x[0]) - x[1]) + x[0] - exp(-x[1])),
        2 * (x[0] * exp(-x[1]) - sin(x[0]) - exp(-2*x[1])+x[1])
    ])

threshhold = 10**-4
start = array([
    [ 5, 2],
    [ 6, 2],
    [-1,-1],
    [-2,-2]
])

for x in start:
    print('x =', x)
    print(' ', steepest_descent(x, f, f_derivative, threshhold))