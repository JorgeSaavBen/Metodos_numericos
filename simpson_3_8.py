import numpy as np

print('Regla de Simpson 3/8')

#Intervalo de integración
a = 0
b = 1

#Segmentos
m = 10
n = 3 * m
h = (b - a)/n

#función a integrar
def f(x):
	f = x**2
	return f
	
#Derivada cuarta
def f4(x):
	f4 = (f(x + 4 * h) - 4 * f(x + 3 * h) + 6 * f(x + 2 * h) - 6 * f(x + h) + f(x)) / (h ** 4)
	return(f4)

x_4 = []

#Área total
A_t = 0

for i in range (1, m + 1):
	x_i0 = a + (3*i - 3) * h
	x_i = a + (3*i - 2) * h
	x_i1 = a + (3*i - 1) * h
	x_i2 = a + (3*i) * h
	
	Ai = 3 * h * (f(x_i0) + 3 * f(x_i) + 3 * f(x_i1) + f(x_i2)) / 8
	A_t = Ai + A_t
	
	if(i == 1):
		x_4.append(abs(f4(x_i0)))
		
	x_4.append(abs(f4(x_i)))
	x_4.append(abs(f4(x_i1)))
	x_4.append(abs(f4(x_i2)))
	
	
#Error
x_4_max = np.max(x_4)
M = x_4_max
E_t = (b - a) * (h ** 4) * (M) / 80
	
print('Área total: ', round(A_t, 10))
print('|Error total|: ', round(E_t, 10)) 
