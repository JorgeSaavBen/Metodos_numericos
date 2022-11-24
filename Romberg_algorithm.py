import numpy as np

print('Algoritmo de Romberg')

a = 1
b = 10

n = 8

R = np.zeros((n, n))

#función a integrar
def f(x):
	f = np.sqrt(x+np.sqrt(x-1))
	return f

R_11 = round((b-a)/2*(f(a)+f(b)), 12)

R[0,0] = R_11

for i in range(1, n):
	for l in range(i+1):
		if(l==0):
			sumator = 0
			for k in range(1, 2**(i-1) + 1):
				sumator = sumator + f(a+(b-a)*(k-1/2)/(2**(i-1)))
			R[i,l] = round((1/2)*(R[i-1, 0]) + ((b-a)/2**(i))*sumator, 12)
		else:
			R[i,l] = round((4**(l)*R[i, l-1] - R[i-1,l-1])/(4**(l)-1), 12)

print(R)
