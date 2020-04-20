# -*- coding: utf-8 -*-

import numpy as np
from LUtils import zerlegung, permutation, vorwaerts, rueckwaerts, greatest_non_zero

def init_for_delta(δ):
    A = np.array([
         [      3,     2,     1],
         [      2, 2 * δ, 2 * δ],
         [      1, 2 * δ,    -δ]
    ])
    
    b = np.array([3 + 3 * δ, 6 * δ, 2 * δ])
    
    return A, b

def correct_answer(δ):
    return np.array([δ, 1, 1])

def calculate_r̃(A, b, x̃):
    return np.subtract(b, np.dot(np.absolute(A), np.absolute(x̃)));

def calculate_s̃(A, b, x̃):
    return np.add(np.dot(np.absolute(A), np.absolute(x̃)), np.absolute(b));
    
def calculate_ɛ(r̃, s̃):
    return np.amax([abs(r̃[i]) / abs(s̃[i]) for i in range(0, len(r̃))])

def calculate_machine_ɛ():
    return (1 / 2) * (2 ** (1 - np.finfo(float).nmant))
    

δ_s = [10**-8, 10**-10,10**-12];

for δ in δ_s:
    print('δ: ', δ)
    
    A, b = init_for_delta(δ)
    LU, p = zerlegung(A, greatest_non_zero)
    p_b = permutation(p, b)
    y = vorwaerts(LU, p_b)
    x̃ = rueckwaerts(LU, y)
    print(x̃)
    print(correct_answer(δ))
          
    r̃ = calculate_r̃(A, b, x̃);
    s̃ = calculate_s̃(A, b, x̃);
    ɛ = calculate_ɛ(r̃, s̃);
    
    kondition = np.linalg.cond(A);
    
    print(' ɛ:  ', ɛ)
    print(' ~ɛ: ', kondition * calculate_machine_ɛ())
    