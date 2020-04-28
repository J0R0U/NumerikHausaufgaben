# -*- coding: utf-8 -*-

import numpy as np
from numpy.linalg import norm, cond

from LUtils import zerlegung, vorwaerts, rueckwaerts, first_non_zero, permutation
from Aufgabe01 import vorwaerts as vorwaerts_T, rueckwaerts as rueckwaerts_T, permutation as permutation_T

def A_for_delta(delta):
  return np.array([[3,2,1],
                   [2,2*delta,2*delta],
                   [1,2*delta,-1*delta]])

def hager(B):
  n = len(B)
  x = np.full(n, 1) / n
  LU, p = zerlegung(B, first_non_zero)
  while True:
    v = vorwaerts_T(LU.T, x)
    w = rueckwaerts_T(LU.T, v)
    y = permutation_T(p, w)
    xi = np.sign(y)
    v = vorwaerts(LU, permutation(p, xi))
    z = np.array(rueckwaerts(LU, v))
    if norm(z, np.inf) <= np.dot(z.T, x):
      return norm(y, 1)
    j = np.argmax(np.abs(z))
    x = np.array([ 1 if k == j else 0 for k in range(len(x)) ])

for delta in [10**-8, 10**-10, 10**-12]:
  A = A_for_delta(delta)
  norm_A = norm(A, np.inf)
  norm_A_inv = hager(A)
  cond_A_approx = norm_A * norm_A_inv
  print(f'cond_approx: {cond_A_approx}')
  print(f'cond: {cond(A)}')
