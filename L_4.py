# Solución para el lab 4

# Los parámetros T, t_final y N son elegidos arbitrariamente

import numpy as np
from scipy import stats
#esta se usa para las gráficas
import matplotlib.pyplot as plt 

# Variables aleatorias A y B para sulucionar y gráficar el ejercicio
va_A = stats.norm(0, np.sqrt(9))
va_B = stats.norm(0, np.sqrt(9))


# Creación del vector de tiempo(se puede dejar igual al ejemplo dado)
# Solo se crea la variable total de elementos y tiempo. 
T = 100			# número de elementos
t_final = 10	# tiempo en segundos
t = np.linspace(0, t_final, T)

# Inicialización del proceso aleatorio X(t) con N realizaciones
N = 10
X_t = np.empty((N, len(t)))	# N funciones del tiempo x(t) con T puntos

# Creación de las muestras del proceso x(t) para A y B independientes
for i in range(N):
	A = va_A.rvs();
	B = va_B.rvs();
	x_t = A * np.cos(np.pi*t + Z);
	X_t[i,:] = x_t;
	plt.plot(t, x_t);
	
	x_t = Y * np.sin(np.pi*t) + X * np.cos(np.pi*t) ;
	X_t[i,:] = x_t;
	plt.plot(t, x_t);

# Promedio de las N realizaciones en cada instante (cada punto en t)
P = [np.mean(X_t[:,i]) for i in range(len(t))]
plt.plot(t, P, lw=6)


# Graficar el resultado teórico del valor esperado
E = 0*t
plt.plot(t, E, '-.', lw=4)

# Mostrar las realizaciones, y su promedio calculado y teórico
plt.title('Realizaciones del proceso aleatorio $X(t)$')
plt.xlabel('$t$')
plt.ylabel('$x_i(t)$')
plt.legend()
plt.show() #mostrar gráficas



# T valores de desplazamiento tau
desplazamiento = np.arange(T)
taus = desplazamiento/t_final

# Inicialización de matriz de valores de correlación para las N funciones
corr = np.empty((N, len(desplazamiento)))

# Nueva figura para la autocorrelación
plt.figure()

# Cálculo de correlación para cada valor de tau
for n in range(N):
	for i, tau in enumerate(desplazamiento):
		corr[n, i] = np.correlate(X_t[n,:], np.roll(X_t[n,:], tau))/T
	plt.plot(taus, corr[n,:])

# Valor teórico de correlación
Rxx = 9 * np.cos(np.pi*taus)

# Gráficas de correlación para cada realización y luego gráficas en el tiempo
plt.plot(taus, Rxx, '-.', lw=4, label='Autocorrelación Teórica')
plt.title('Funciones de autocorrelación de las realizaciones del proceso')
plt.xlabel(r'$\tau$')
plt.ylabel(r'$R_{XX}(\tau)$')
plt.legend()
plt.show()

plt.plot(t, corr[n,:], lw=6, color = 'blue', label='Autocorrelación experimental')
plt.plot(t, Rww, '-.', lw=4, color='lime')
plt.title('Funciones de autocorrelación en el tiempo')
plt.xlabel(r'$t$')
plt.ylabel(r'$R_{XX}(\tau)$')
plt.legend()
plt.show()    
