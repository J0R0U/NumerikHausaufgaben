# -*- coding: utf-8 -*-

import numpy as np
from LUtils import first_non_zero, zerlegung

def permutation(p, x):
  for index, perm in reversed(list(enumerate(p))):
    x[index], x[perm] = x[perm], x[index]
  return x

def vorwaerts(LU_T, c):
  # U_T * v = c
  res = []
  for y in range(len(LU_T)):
    res.append((c[y] - sum([ LU_T[y,x] * res[x] for x in range(y) ])) / LU_T[y,y] )
  return res

def rueckwaerts(LU_T, v):
  # L_T * w = v
  res = np.zeros(len(LU_T))
  for y in range(len(LU_T)-1, -1, -1):
    res[y] = v[y] - sum([ LU_T[y,x] * res[x] for x in range(y+1, len(LU_T))])
  return res

if __name__ == '__main__':
  A = np.array([[0,0,0,1],
                [2,1,2,0],
                [4,4,0,0],
                [2,3,1,0]])

  c = np.array([152,154,56,17])

  print(f'A: {A}')
  print(f'c: {c}')

  LU, p = zerlegung(A, first_non_zero)
  print(f'LU: {LU}')
  print(f'p: {p}')
  v = vorwaerts(LU.T, c)
  print(f'v: {v}')
  w = rueckwaerts(LU.T, v)
  z = permutation(p, w)

  print('Ergebnis:')
  print(f'z: {z}')
