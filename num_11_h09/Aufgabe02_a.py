# -*- coding: utf-8 -*-

from utils import calcDevidedDeltas, calcInterploationPolynom

points = [
    [0, 3],
    [1, 2],
    [3, 6]
]
x = 2

devidedDeltas = calcDevidedDeltas(points)
y = calcInterploationPolynom(2, devidedDeltas)

print('x: ', x, ', p(x)=', y)
