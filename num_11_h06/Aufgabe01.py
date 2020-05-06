import numpy as np
import matplotlib.pyplot as plt
from ex06_lib import system, plotxk

def cg(A, b):
    x = np.zeros(A.shape[0])
    p = np.subtract(b, A.dot(x))
    r_0 =p
    r = p
    plot_data = [1]
    
    while plot_data[-1] > 10**-6:
        alpha = r.dot(r) / p.dot(A.dot(p))
        new_r = np.subtract(r, alpha * A.dot(p))
        beta  = new_r.dot(new_r) / r.dot(r)
        new_p = np.add(new_r,beta * p)
        
        x = x + alpha * p
        r = new_r
        p = new_p
        plot_data.append(np.linalg.norm(r) / np.linalg.norm(r_0))
    
    return x, plot_data


m_s = [50, 100, 200]
for idx in range(0, len(m_s)):
    A,b = system(m_s[idx])
    x, plot_data = cg(A,b)
    
    plt.semilogy(plot_data)
    plt.text(m_s[idx], 8, 'm=' + str(m_s[idx]))
    plt.xlabel('Iteration')
    plt.ylabel('normierte Residuen')
    plt.show()
    
    plotxk(x)
    plt.show()