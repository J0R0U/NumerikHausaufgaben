# -*- coding: utf-8 -*-

import numpy as np

def first_non_zero(A, p, k, n, curr):
    if A[curr][curr] == 0:
        for j in range(k, n):
            if A[j][curr] != 0:
                A[[curr,j]] = A[[j, curr]]
                p[curr] = j
                break

def greatest_non_zero(A, p, k, n, curr):
    max_index = curr
    for j in range(k, n):
            if abs(A[j][curr]) > abs(A[max_index][curr]):
                max_index = j;

    A[[curr,max_index]] = A[[max_index, curr]]
    p[curr] = max_index

def zerlegung(A, swap_function):
    A = A.copy()
    n = len(A)
    p = []
    for k in range(1, n):
        curr = k - 1
        p.append(curr)

        swap_function(A, p, k, n, curr)

        for y in range(k, n):
            l = (A[y][curr] / A[curr][curr])
            for x in range(k, n):
                A[y][x] -= l * A[curr][x]
            A[y][curr] = l
    return A, p

def permutation(p, x):
    for index, perm in enumerate(p):
        x[index], x[perm] = x[perm], x[index]
    return x

def vorwaerts(LU, b):
    res = []
    for y in range(len(LU)):
        res.append((b[y] - sum([ LU[y,x] * res[x] for x in range(y)])))
    return res

def rueckwaerts(LU, b):
    res = [ 0 for i in range(len(LU)) ]
    for y in range(len(LU)-1, -1, -1):
        res[y] = (b[y] - sum([ LU[y,x] * res[x] for x in range(y+1, len(LU))])) / LU[y,y]
    return res

def nachiteration(A, b, LU, p, x):
    x_k = x
    
    for i in range(10):
        r_k = np.subtract(b, np.dot(A, x_k))
        
        r_k_p = permutation(p, r_k)
        y = vorwaerts(LU, r_k_p)
        p_k = rueckwaerts(LU, y)
        
        tmp = np.add(x_k, p_k);
        x_k = tmp
    
    return np.add(x, p_k)
