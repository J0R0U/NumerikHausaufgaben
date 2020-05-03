# -*- coding: utf-8 -*-

import numpy as np
from LUtils import greatest_non_zero, zerlegung, permutation, vorwaerts, rueckwaerts, nachiteration
    
def create_a_b_exercise_a(n):
    A = np.array([np.array([1 if i == j or j == n - 1 else -1 if j < i else 0 for j in range(n)]) for i in range(n)], dtype=float)
    b = np.array([2 - i for i in range(n - 1)] + [2- n], dtype=float)
    
    return A, b

def exercise_a():
    for n in [40, 50, 60]:
        print(n, ":")
        
        A, b = create_a_b_exercise_a(n)
        LU, p = zerlegung(A, greatest_non_zero)
        x = permutation(p, b)
        y = vorwaerts(LU, x)
        z = rueckwaerts(LU, y)
        
        print(nachiteration(A, b, LU, p, z))
        
  
def create_a_b_exercise_b(n):
    A = np.array([np.array([1 if j == i else 0 if j > i else i + j for j in range(1, n + 1)]) for i in range(1, n + 1)], dtype=float)
    b = np.array([1] + [0 for i in range(n - 1)], dtype=float)
    return A, b

def exercise_b():
    for n in range(10, 16):
        print(n, ":")
        
        A, b = create_a_b_exercise_b(n)
        LU, p = zerlegung(A, greatest_non_zero)
        x = permutation(p, b)
        y = vorwaerts(LU, x)
        z = rueckwaerts(LU, y)
        
        print(nachiteration(A, b, LU, p, z))

exercise_a()
exercise_b()