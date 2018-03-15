import numpy as np
file = np.loadtxt('monthrg.dat')
x = file[:, 0] + (file[:, 1]-1)/12.0
y = file[:, 3]
ii = x>1900
salida = np.array([x[ii], y[ii]])
np.savetxt('fecha_manchas.dat', salida.T)

