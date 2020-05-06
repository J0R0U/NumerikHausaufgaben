# -*- coding: utf-8 -*-

import numpy as np
from math import sqrt
from ex06_lib import Ablock, ew_exakt, plotev, animev

def sign(t):
    return -1 if t < 0 else 1

def qs_nde(A):
    ret = 0
    
    for i in range(0, len(A) - 1):
        ret += np.sum([A[i][j] ** 2 for j in range(i + 1, len(A[i]))])
                
    return ret * 2

def search_i_j(A):
    max_i = 0
    max_j = 1
    
    for i in range(0,len(A) - 1):
        max_in_row = np.argmax([abs(A[i][j]) for j in range(i + 1, len(A[i]))]) + i + 1
        if(abs(A[i][max_in_row]) > abs(A[max_i][max_j])):
            max_i = i;
            max_j = max_in_row;
                
    return max_i, max_j
    
def jacobi(A, e):
    A = np.copy(A)
    Q_total = np.identity(len(A), dtype=float);
    
    while sqrt(qs_nde(A)) > e:      
        i_0, j_0 = search_i_j(A)
        a = (A[j_0][j_0] - A[i_0][i_0]) / (2 * A[i_0][j_0])
        c = sqrt(1/2 + 1/2 * sqrt(a ** 2 / (1 + a ** 2)))
        s = sign(a) / (2 * c * sqrt(1 + a**2))
        
        Q = np.identity(len(A));
        Q[i_0][i_0], Q[j_0][j_0], Q[j_0][i_0], Q[i_0][j_0] = c, c, -s, s
        
        A = Q.transpose().dot(A.dot(Q))
        Q_total = Q_total.dot(Q)
    
    ret = []
    for i in range(0,len(A)):
        ret.append([A[i][i], Q_total[:,i]])
    return ret

m = 10

A = Ablock(m)

ew_ev_num = jacobi(A, 10**-3)
ew_ev_num.sort(key=lambda x : x[0])

ew_exact = ew_exakt(m)
ew_exact.sort()

for idx in range(0, len(ew_ev_num)):
    ew = ew_ev_num[idx][0]
    
    print('Eigenwert (num):   ', ew)
    print('Eigenwert (exact): ', ew_exact[idx])
    print()
        
    if(idx < 4):
        ev = ew_ev_num[idx][1]
        plotev(ev)

animev(ew_ev_num[0][1])()