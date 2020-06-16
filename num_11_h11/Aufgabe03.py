# -*- coding: utf-8 -*-

from math import sqrt, pi, exp

import numpy as np
import scipy as sp

def create_a(n, g):
    c = 1 / (g * sqrt(2 * pi))
    exponential = lambda i, j: exp(-((i - j)/(sqrt(2) * n * g))**2)
    
    return np.array(
        [[(c / n) * exponential(i, j) for j in range(0, n)] for i in range(0, n)]
    )

def create_x(n):
    return np.array(
        [1 if 45 <= i and i <= 55 else 0.5 if 60 <= i and i <= 65 else 0 for i in range(0, n)]
    )

def random_vec(n, scale):
    return np.random.randn(n) * scale
    
def solve_with_pinv(A, b_disturbed):
    return np.linalg.pinv(A).dot(b_disturbed)

def TSVD(A, b_disturbed, a):
    n, m = len(A[0]), len(A)
    
    U, s, V = sp.linalg.svd(A, full_matrices=True)
    
    s = [s[len(s) - 1 - i] for i in range(0, len(s))]
    s = [s[i] if s[0] / s[i] <= 1 / a else 0 for i in range(0, len(s))]
    
    print(s)
    
    E = np.array([[0 if i != j else s[len(s) - 1 - i] for j in range(0, n)] for i in range(0, m)])
    
    U_len = len(U)
    for i in range(0, (int) (U_len / 2)):
        tmp                = U[:,i].copy()
        U[:,i]             = U[:,U_len - 1 - i]
        U[:,U_len - 1 - i] = tmp
    
    V_len = len(V)
    for i in range(0, (int) (V_len / 2)):
        tmp                = V[:,i].copy()
        V[:,i]             = V[:,V_len - 1 - i] 
        V[:,V_len - 1 - i] = tmp
    
    return V.dot(np.linalg.pinv(E).dot(U.transpose()).dot(b_disturbed))

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