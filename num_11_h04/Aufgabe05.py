# -*- coding: utf-8 -*-

import numpy as np
from numpy.linalg import norm

from LUtils import vorwaerts, permutation, zerlegung, greatest_non_zero, rueckwaerts

def householder(A, b):
  diag = []
  orig_A = np.copy(A)
  temp_A = np.copy(A)
  Q_cumulative = np.identity(len(A))
  for x in range(len(A)):
    n = len(A) - x
    a = A[x:, x]
    if len(a) == 1:
      diag.append(*a)
      break
    norm_a = norm(a, 2)
    d = -np.sign(a[0]) * norm_a
    v1 = a[0] - d
    norm_v_sq = -2 * v1 * d
    v = np.array([v1, *a[1:]])[:,np.newaxis]
    Q = np.identity(n) - 2 / ( norm_v_sq ) * v * v.T
    Q_ext = np.identity(len(A))
    Q_ext[x:,x:] = Q
    Q_cumulative = np.dot(Q_ext, Q_cumulative)
    A = np.dot(Q_ext, A)
    diag.append(d)
    temp_A[x:,x] = v.reshape(n)

  Q = Q_cumulative.T
  R = np.dot(Q_cumulative, orig_A)
  y = np.dot(Q.T, b)
  x = vorwaerts(R, y)
  return x

def init_A_b(n):
  A = np.identity(n)
  for y in range(1, n):
    for x in range(y):
      A[y,x] = -1;
  A[:,-1] = 1
  b = np.array([ 2 - n  if i == n else 3 - i for i in range(n) ])
  return A, b


if __name__ == '__main__':
  A = np.array([[20,18,44],
                [0,40,45],
                [-15,24,-108]])
  b = np.array([-4, -45, 78])

  x = householder(A, b)
  print(x)

  for n in [40,50,60]:
    A, b = init_A_b(n)

    x = householder(A, b)
    print(f'n={n}: {x}')

    LU, p = zerlegung(A, greatest_non_zero)
    x = permutation(p, b)
    y = vorwaerts(LU, x)
    res = rueckwaerts(LU, y)
    print(res)

