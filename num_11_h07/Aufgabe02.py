import numpy as np
from math import sqrt

from ex06_lib import Ablock, ew_exakt

def calculate_u(A, n):    
    
    root = sqrt((A[n-1][n-1] + A[n][n]) ** 2 / 4 + A[n-1][n] * A[n][n-1] - A[n][n] * A[n-1][n-1]);
    
    one = (A[n-1][n-1] + A[n][n]) / 2 + root
    two = (A[n-1][n-1] + A[n][n]) / 2 - root
    
    if abs(one - A[n][n]) < abs(two - A[n][n]):
        return one
    else:
        return two

def qr_iteration(A, e):
    n = len(A)
    
    A = A.copy()
    Q = np.identity(n)
    
    curr_n = n - 1
    
    while curr_n > 1:
        while abs(A[curr_n][curr_n - 1]) > e:
            u = calculate_u(A, curr_n)
            
            Q_k, R_k = np.linalg.qr(A - u * np.identity(n))
            
            A = R_k.dot(Q_k) + u * np.identity(n)
            Q = Q.dot(Q_k)
            
        curr_n = curr_n - 1
    
    return [[A[i][i], Q[:,i]] for i in range(n)]

m = 10
A = Ablock(m)

ew_ev_num = qr_iteration(A, 10**-9)
ew_ev_num.sort(key=lambda x : x[0])

ew_exact = ew_exakt(m)
ew_exact.sort()

for idx in range(0, len(ew_ev_num)):
    ew = ew_ev_num[idx][0]
    
    print(idx, ':')
    print('  Eigenwert (num):   ', ew)
    print('  Eigenwert (exact): ', ew_exact[idx])
    print()