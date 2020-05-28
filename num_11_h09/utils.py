# -*- coding: utf-8 -*-

def calcDevidedDeltas(points):
    ret = points.copy()
    lenOfRet = len(ret)
    
    for n in range(0,lenOfRet):
        for m in range(1, n + 1):
            ret[n].append((ret[n][m]-ret[n-1][m]) / (ret[n][0]- ret[n - m][0]))
    
    return ret

def calcInterploationPolynom(x, devidedDeltas):
    lenOfDeltas = len(devidedDeltas)
    q = devidedDeltas[lenOfDeltas - 1][-1]
    
    for k in range(1, lenOfDeltas):
        q = devidedDeltas[lenOfDeltas - 1 - k][-1] + (x - devidedDeltas[lenOfDeltas - 1 - k][0]) * q
    
    return q
