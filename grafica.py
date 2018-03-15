import matplotlib.pyplot as plt
import numpy as np
archivo = np.loadtxt("fecha_manchas.dat")
plt.plot(archivo[:,0], archivo[:,1])
plt.savefig('fecha_manchas.pdf')
