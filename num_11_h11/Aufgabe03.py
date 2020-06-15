# -*- coding: utf-8 -*-

from numpy import array, linalg, random
from math import sqrt, pi, exp

def create_a(n, g):
    c = 1 / (g * sqrt(2 * pi))
    exponential = lambda i, j: exp(-((i - j)/(sqrt(2) * n * g))**2)
    
    return array(
        [[(c / n) * exponential(i, j) for j in range(0, n)] for i in range(0, n)]
    )

def create_x(n):
    return array(
        [1 if 45 <= i and i <= 55 else 0.5 if 60 <= i and i <= 65 else 0 for i in range(0, n)]
    )

def random_vec(n, scale):
    return random.randn(n) * scale
    
def solve_with_pinv(A, b_disturbed):
    return linalg.pinv(A).dot(b_disturbed)

def TSVD(A, b_disturbed, a):
    U = ;
    E = ;
    V = ;
    
    return U.dot(E).dot(V.transpose())

n = 100
g = 0.05
d = 10**-6
k_s = range(0, -9, -1)

A = create_a(n, g)
x = create_x(n)

b = A.dot(x)
b_disturbed = b + random_vec(n, d)

print(x)
print(solve_with_pinv(A, b_disturbed))

for k in k_s:
    print(TSVD(A, b_disturbed, 10**k))