# -*- coding: utf-8 -*-

import numpy as np
from LUtils import zerlegung, permutation, vorwaerts, rueckwaerts

def exercise_one():
    A = np.array([[0,0,0,1],[2,1,2,0],[4,4,0,0],[2,3,1,0]])
    b_one = np.array([ 3, 5, 4, 5])
    b_two = np.array([ 4,10,12,11])
    
    LU, p = zerlegung(A)
    
    pb = permutation(p, b_one)
    y  = vorwaerts(LU, pb)
    print(rueckwaerts(LU, y))
    
    pb = permutation(p, b_two)
    y  = vorwaerts(LU, pb)
    print(rueckwaerts(LU, y))
    
def exercise_two():
    for n in [5,10,15,20]:
        A = np.array([[1/(i+j-1) for j in range(1,n+1)] for i in range(1,n+1)])
        b = np.array([1/(i+1) for i in range(1,n+1)])
        LU, p = zerlegung(A)
        pb = permutation(p, b)
        y = vorwaerts(LU, pb)
        print('n:', n, '=>', rueckwaerts(LU, y))

exercise_one()
exercise_two()