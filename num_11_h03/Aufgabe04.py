# -*- coding: utf-8 -*-

import numpy as np
from LUtils import zerlegung, permutation, vorwaerts, rueckwaerts, first_non_zero, greatest_non_zero

def init_row(n, beta, i):
    if (i == 0):
        return np.array([1] + [ 0 for j in range(0, n - 2)] + [beta])
    elif (i == n - 1):
        return np.array([(-beta if j == n - 2 else 0) for j in range(0, n)])
    else:
        return np.array([( 1 if i == j else -beta if i - 1 == j else 0) for j in range(0, n)])

def init_for_n(n, beta):   
    A = np.array([init_row(n, beta, i)  for i in range(0, n)], dtype=float)
    b = np.array([1 + beta] + [1 - beta for i in range(0, n - 2)] + [-beta], dtype=float)
    return A, b

def without_pivot_search(n, beta):
    A, b = init_for_n(n, beta)
    LU, p = zerlegung(A, first_non_zero)
    x = permutation(p, b)
    y = vorwaerts(LU, x)
    return rueckwaerts(LU, y)

def with_pivot_search(n, beta):
    A, b = init_for_n(n, beta)
    LU, p = zerlegung(A, greatest_non_zero)
    x = permutation(p, b)
    y = vorwaerts(LU, x)
    return rueckwaerts(LU, y)

def correct_answer(n):
    return np.full(n, 1)

b_s = np.array([10])
n_s = np.array([10,15,20])

for b in b_s:
    for n in n_s:
        print('b: ', b, ', n: ', n)
        print('without: ', without_pivot_search(n, b))
        print('with:    ', with_pivot_search(n, b))
        print('correct: ', correct_answer(n))
    

