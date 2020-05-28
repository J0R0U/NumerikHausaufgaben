# -*- coding: utf-8 -*-

from utils import calcDevidedDeltas, calcInterploationPolynom
from numpy import arange
from math import cos, pi
import matplotlib.pyplot as plt

def f(x):
    return 1 / (1 + x**2)

def calculatePointsEquidistant(m):
    ret = []
    delta = 10 / (m + 1);
    
    for i in range(0, m):
        x = -5 + (i + 1) * delta
        ret.append([x, f(x)])
        
    return ret

def calculatePointsSpecialNotEquidistant(m):
    ret = []
    
    for i in range(0, m):
        x = -5 * cos(pi * (2 * i + 1) / (2 * m))
        ret.append([x, f(x)])
        
    return ret

m_s = [7, 9, 11]
x_vals = arange(-5, 5.01, 0.01)

for m in m_s:
    plt.subplot(2,1,1)
    plt.title('equidistant')
    plt.plot(x_vals, f(x_vals))
    points = calculatePointsNormal(m);
    devidedDeltas = calcDevidedDeltas(points)
    f_inter = lambda x: calcInterploationPolynom(x, devidedDeltas)
    plt.plot(x_vals, f_inter(x_vals))    
    plt.scatter([row[0] for row in points], [row[1] for row in points], label= "stars", color= "green", marker= "*", s=30) 
    
    plt.subplot(2,1,2)
    plt.title('not equidistant')
    plt.plot(x_vals, f(x_vals))    
    points = calculatePointsSpecial(m);
    devidedDeltas = calcDevidedDeltas(points)
    f_inter = lambda x: calcInterploationPolynom(x, devidedDeltas)
    plt.plot(x_vals, f_inter(x_vals))
    plt.scatter([row[0] for row in points], [row[1] for row in points], label= "stars", color= "green", marker= "*", s=30) 
    
    plt.tight_layout()
    plt.show()
