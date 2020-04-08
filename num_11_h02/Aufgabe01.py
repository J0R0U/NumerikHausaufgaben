# -*- coding: utf-8 -*-

import numpy as np

def zerlegung(A):
    n = len(A)
    p = []
    for k in range(1, n):
        curr = k - 1
        p.append(curr)
        # swap if diagonal element is 0
        if A[curr][curr] == 0:
            for j in range(k, n):
                if A[j][curr] != 0:
                    A[[curr,j]] = A[[j, curr]]
                    p[curr] = j
                    break

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
        res.append((b[y] - sum([ LU[y,x] * res[x] for x in range(y) ])))
    return res

def rueckwaerts(LU, b):
    res = [ 0 for i in range(len(LU)) ]
    for y in range(len(LU)-1, -1, -1):
        res[y] = (b[y] - sum([ LU[y,x] * res[x] for x in range(y+1, len(LU)) ])) / LU[y,y]
    return res

A = np.array([[0,0,0,1],[2,1,2,0],[4,4,0,0],[2,3,1,0]])
b = np.array([3,5,4,5])
print(A)
LU, p = zerlegung(A)
pb = permutation(p, b)
y = vorwaerts(LU, pb)
print(y)
print(rueckwaerts(LU, y))

for n in [5,10,15,20]:
    A = np.array([[1/(i+j-1) for j in range(1,n+1)] for i in range(1,n+1)])
    b = np.array([1/(i+1) for i in range(1,n+1)])
    LU, p = zerlegung(A)
    pb = permutation(p, b)
    y = vorwaerts(LU, pb)
    print('n:', n, '=>', rueckwaerts(LU, y))
