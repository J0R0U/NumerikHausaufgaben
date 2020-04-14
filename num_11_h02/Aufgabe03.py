# -*- coding: utf-8 -*-
import math

def zerlegung(n):
    for k in range(n-1):
        dia[k] = math.sqrt(dia[k])
        subdia[k] = subdia[k]/dia[k]
        dia[k+1] = dia[k+1]-subdia[k]**2
    dia[n-1] = math.sqrt(dia[n-1])

def vorwaerts(n):
    b[0] = b[0]/dia[0]
    for j in range(1,n):
        b[j] = (b[j]-b[j-1]*subdia[j-1])/dia[j]

def rueckwaerts(n):
    b[n-1] = b[n-1]/dia[n-1]
    for k in range(n-2,-1,-1):
        b[k] = (b[k]-b[k+1]*subdia[k])/dia[k]
        
for n in [4, 100, 1000, 10000]:
    
    dia = []
    subdia = []
    b = []
    
    for i in range(n):
        dia.append(2)
        b.append(-1/(n+1)**2)
        
    for i in range(n-1):
        subdia.append(-1)

    zerlegung(n)
    vorwaerts(n)
    rueckwaerts(n)
    print (b)

