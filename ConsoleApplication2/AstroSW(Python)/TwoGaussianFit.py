import matplotlib.pyplot as pt
import numpy as np
from scipy.optimize import leastsq

####################################
# Setting up test data

def norm(x, media, sd):
    norm = []

    for i in range(x.size):
        norm += [1.0/(sd*np.sqrt(2*np.pi))*np.exp(-(x[i] - media)**2/(2*sd**2))]
    return np.array(norm)

media1 = 0
media2 = -2
std1 = 0.5
std2 = 1

x = np.linspace(-20, 20, 500)
y_real = norm(x, media1, std1) + norm(x, media2, std2)

######################################
# Solving

m, dm, sd1, sd2 = [5, 10, 1, 1]
p = [m, dm, sd1, sd2] # Initial guesses for leastsq
y_init = norm(x,m,sd1) + norm(x, m + dm, sd2) # For final comparison plot

def res(p, y, x):
    m, dm, sd1, sd2 = p

    m1 = m
    m2 = m1 + m
    y_fit = norm(x, m1, sd1) + norm(x, m2, sd2)
    error = y - y_fit

    return error

plsq = leastsq(res, p, args = (y_real, x))

y_est = norm(x, plsq[0][0], plsq[0][2]) + norm(x, plsq[0][0] + plsq[0][1], plsq[0][3])
