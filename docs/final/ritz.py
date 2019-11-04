import sympy as sm
import numpy as np
from matplotlib import pyplot as plt

# polynomial function

plt.figure()
x,q,E,I,L = sm.symbols('x q E I L')
xs = np.linspace(0,1)
for i in range(1,4):
	w = 0
	a = []
	for j in range(i):
		a.append(sm.symbols('a'+str(j)))
#		w = w + a[j]*x**(j+1)*(L-x)
		w = w + a[j]*sm.sin((j+1)*sm.pi*x/L)
	Pi = sm.integrate(E*I/2*sm.diff(w,x,x)**2-q*w,(x,0,L)) 
	eqns = []
	vals = []
	for j in range(i):
		eqns.append(sm.diff(Pi,a[j]))
		vals.append(a[j])
	ans = sm.solve(eqns,vals)
	print Pi
	print ans
	for j in range(i):
		w = w.subs(ans.items())
	print w
	wl = sm.lambdify(x,w.subs([(q,1),(E,1),(I,1),(L,1)]))
	plt.plot(xs,[wl(k) for k in xs],label='Sin Ritz N=%d'%i)

plt.plot(xs,xs/24*(1+ xs**3-2*xs**2),'k--',label='exact')
plt.legend(loc='best')
plt.xlabel('x/L')
plt.ylabel('EI/q w')
plt.show()