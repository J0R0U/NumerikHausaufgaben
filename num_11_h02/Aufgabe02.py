# -*- coding: utf-8 -*-

import numpy as np
from LUtils import zerlegung, permutation, vorwaerts, rueckwaerts

A = np.array([[0,0,0,1],[2,1,2,0],[4,4,0,0],[2,3,1,0]])

u = np.array([0,1,2,3])
v = np.array([0,0,0,1])

b = np.array([3,5,4,5])

LU, p = zerlegung(A)

per = permutation(p, u)
y = vorwaerts(LU, per)
z = rueckwaerts(LU, y)

val = 1 + np.dot(np.transpose(v),z)
if val != 0:
    a = 1 / val
    per = permutation(p, b)
    y = vorwaerts(LU, per)
    z_dach = rueckwaerts(LU, y)
    print(z_dach - a * np.dot(np.dot(np.transpose(v),z_dach), z))
    
    